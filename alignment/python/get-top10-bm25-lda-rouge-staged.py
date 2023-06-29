#!usr/bin/python3
# encoding: utf-8

import sys
sys.setrecursionlimit(2000)
import warnings
warnings.filterwarnings("ignore")

import re
import json
import nltk
import click
import itertools
import numpy as np
import multiprocessing as mp
from typing import List
from pathlib import Path
from tqdm.auto import tqdm
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
from rank_bm25 import BM25Okapi
from rouge import Rouge
from gensim.corpora import Dictionary
from operator import itemgetter
from gensim.models import HdpModel, LdaMulticore
from gensim.matutils import cossim, hellinger

rouge = Rouge()
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer() 
 
def preprocess(sentence):
    '''
    preprocess text for LDA modeling
    '''
    sentence = sentence.lower()
    tokenized = word_tokenize(sentence)
    tokens = [t for t in tokenized if t.isalnum()]
    filtered_words = [w for w in tokens if not w in stopwords.words('english')]
    stem_words = [stemmer.stem(w) for w in filtered_words]
    lemma_words = [lemmatizer.lemmatize(w) for w in stem_words]
    return lemma_words


def read_data(filename: str):
    with open(filename, 'r') as f:
         data = f.readlines()
         index = [t.split('\t')[0] for t in data]
         corpus = [t.split('\t')[1].replace('Table of Contents', "") for t in data]
         tokenized_corpus = [preprocess(t) for t in corpus]
    return {'index': index, 'corpus': corpus, 'tokenized_corpus': tokenized_corpus}


def get_rouge(query: str, pool: list) -> np.array:
    sentences = [query] * len(pool)
    rouge_scores = np.array([d['rouge-2']['f'] for d in rouge.get_scores(sentences, pool)])
    # rouge_scores /= rouge_scores.max() if rouge_scores.max() > 0 else rouge_scores
    return rouge_scores


def get_sub_sequence(lst: List[dict]) -> List[dict]:
    
    lst = sorted(lst, key=lambda x: x['rouge-2'], reverse=True)
    
    rouges = [i['rouge-2'] for i in lst]
    rouge_diffs = [abs(rouges[i] - rouges[i - 1]) for i in range(1, len(rouges))]
    rouge_max_diff = max(rouge_diffs)
    
    output = [lst[0]]
    for i in range(1, len(rouges)):
        if rouge_diffs[i - 1] < rouge_max_diff:
            output.append(lst[i])
        else:
            break
    
    return output


class LDA:
    def __init__(self, index, corpus, tokenized_corpus):
        self.index = index
        self.corpus = corpus
        self.tokenized_corpus = tokenized_corpus
         
        self.dictionary = Dictionary(self.tokenized_corpus)
        self.bow_corpus = [self.dictionary.doc2bow(doc) for doc in self.tokenized_corpus]
        
        self.lda = HdpModel(self.bow_corpus, self.dictionary)
        self.lda_corpus = [self.lda[bow] for bow in self.bow_corpus]

    def get_topic_distribution(self, sentence):
        tokenized_sentence = preprocess(sentence)
        bow_sentence = self.dictionary.doc2bow(tokenized_sentence)
        topic_distribution = self.lda[bow_sentence]
        return topic_distribution


def bm25_normalization(tokenized_query):
    # calculate "maximum" in bm25:
    bm25_scores = bm25.get_scores(tokenized_query)
    bm25_max_score = 0
    query_len = len(tokenized_query)
    for q in set(tokenized_query):
        q_freq = sum([term == q for term in tokenized_query])
        bm25_max_score += (bm25.idf.get(q) or 0) * (q_freq * (bm25.k1 + 1) /
                     (q_freq + bm25.k1 * (1 - bm25.b + bm25.b * query_len / bm25.avgdl)))
    bm25_scores /= bm25_max_score # local

    return bm25_scores

   


def get_hit_result(qid, data, lda, corpus_ids, corpus, tokenized_corpus, lda_corpus, bm25):
    query_index = data['index'][qid]
    query = data['corpus'][qid]
    tokenized_query = data['tokenized_corpus'][qid] # global
    lda_query = lda.lda_corpus[qid]
            
    bm25_scores = bm25.get_scores(tokenized_query)

    lda_scores = 1 - (np.array([hellinger(lda_query, lda_sent) for lda_sent in lda_corpus]))# + 1) / 2 # local
    rouge_scores = get_rouge(query, list(corpus)) # local
    
    result = [{'rouge-2': r, 'bm25': b, 'lda-hellinger': h}
               for r, b, h in zip(rouge_scores, bm25_scores, lda_scores)]
    
    # final_scores = bm25_scores + lda_scores + rouge_scores # len = corpus

    # sort by bm25/rouge-2
    # argmaxs = np.argpartition(bm25_scores, -10)[-10:] # get top10
    # re-calculate looks so dumb
    # TODO: when n < 10 the bug will arise
    topk = min(10, len(rouge_scores))
    argmaxs = np.argpartition(rouge_scores, -topk)[-topk:] # get top10
    argmaxs = [i[0] for i in sorted(list(zip(argmaxs, rouge_scores[argmaxs])), key=lambda x: x[1], reverse=True)] # sort top10
            
    hit_ids = itemgetter(*argmaxs)(corpus_ids) # global
    hit_index = itemgetter(*hit_ids)(data['index'])
    hit_result = [{'last-year-id': i, 'rouge-2': r, 'bm25': b, 'lda': l} 
                   for i, r, b, l in zip(hit_index, 
                                         rouge_scores[argmaxs], 
                                         bm25_scores[argmaxs],
                                         lda_scores[argmaxs])]
    return (query_index, hit_result, result)


@click.command()
@click.option('--filename', '-f', help='file contains lines of INDEX<TAB>segments, which come from same item from a company across different years') 
@click.option('--output_dir', '-o', help='directory for saving results, which are .json files named CIK_year_ITEM')
@click.option('--record_dir', '-r', help='directory for recording')
def main(filename, output_dir, record_dir):
    company = Path(filename).stem
    data = read_data(filename)
    if not data['index']:
        return
    # LDA model is trained across year: one company one LDA model
    lda = LDA(data['index'], data['corpus'], data['tokenized_corpus'])

    years = sorted(set([i.split('_')[1] for i in data['index']]))
    for year in tqdm(years[1:]):
        last_year = str(int(year) - 1)
        queries_ids = [i for i in range(len(data['index'])) if f'{year}' == data['index'][i].split('_')[1]] 
        # global qid
        corpus_ids = [i for i in range(len(data['index'])) if f'{last_year}' == data['index'][i].split('_')[1]] 
        # global cid
        if queries_ids == []:
            print(company, year, "item7 is missed!")
            continue
        if corpus_ids == []:
            print(company, int(year) - 1, "item7 is missed!")
            continue
        corpus = itemgetter(*corpus_ids)(data['corpus']) # tuple
        tokenized_corpus = itemgetter(*corpus_ids)(data['tokenized_corpus'])
        lda_corpus = itemgetter(*corpus_ids)(lda.lda_corpus)

        bm25 = BM25Okapi(tokenized_corpus)
        
        global wrapper
        def wrapper(qid):
            return get_hit_result(qid, data, lda, corpus_ids, corpus, tokenized_corpus, lda_corpus, bm25)
        
        try: 
            pool_obj = mp.Pool(40)
            answer = pool_obj.map(wrapper, queries_ids)
            # to_write = list(itertools.chain.from_iterable(answer))
        except RecursionError or ValueError:
            print(company, year, 'raise recursion error!') 
        
        to_write = {i: result for i, result, _ in answer}
        record = [r[2] for r in answer]

        with open(f'{output_dir}{"_".join(list(to_write.keys())[0].split("_")[:3])}.json', 'w') as f:
        # with open(f'{output_dir}/{company}_{year}.json', 'w') as f:
            json.dump(to_write, f, indent=2, ensure_ascii=False)

        with open(f'{record_dir}{"_".join(list(to_write.keys())[0].split("_")[:3])}.json', 'w') as f:
            json.dump(record, f, indent=2, ensure_ascii=False)
        


if __name__ == '__main__':
    main()

# texts = ['hi, this is 2016. I wish I\'ll be happier', 'oh no this is 2018']
# print([preprocess(t) for t in texts])
