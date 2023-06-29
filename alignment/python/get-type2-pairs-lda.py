import os
import ndjson
import json
import click
from tqdm.auto import tqdm

# 0.5568      0.7536
@click.command()
@click.option('--directory', '-d', help='directory contain files after get-sbert-cossim')
@click.option('--corpus', '-c', help='pool contain all INDEX<TAB>segments')
@click.option('--rouge_sim_threshold', '-rs', type=float, default=0.6038)
@click.option('--sbert_neg_threshold', '-sn', type=float, default=0.7536)
@click.option('--lda_neg_threshold', '-ln', type=float, default=0.5568)
@click.option('--print_type1', '-pt1', type=bool, default=True)
def main(directory, corpus, rouge_sim_threshold, sbert_neg_threshold, lda_neg_threshold, print_type1):
    
    corpus_dict = dict()
    with open(corpus) as f:
        for line in tqdm(f):
            try:
                idx, sentence = line.split('\t')
                corpus_dict[idx.lower()] = sentence.strip()
            except ValueError:
                pass
    record = []
    for filename in tqdm(os.listdir(directory)):
        # last-year-id, rouge-2, bm25, lda, sbert
        with open(directory + '/' + filename, 'r') as f:
            data = ndjson.load(f)
        for line in data:
            this_year_ID = line[0].lower()
            last_year_ID = line[1].lower()
            rouge = line[2]
            bm25 = line[3]
            lda = line[4]
            sbert = line[5]

            if rouge <= rouge_sim_threshold:
                if print_type1:
                    print(f'TYPE_1\t{last_year_ID}\t{this_year_ID}\t{corpus_dict[last_year_ID]}\t{corpus_dict[this_year_ID]}')
            elif rouge > rouge_sim_threshold and sbert < sbert_neg_threshold: # or lda < lda_neg_threshold:
                print(f'{last_year_ID}\t{this_year_ID}\t{corpus_dict[last_year_ID]}\t{corpus_dict[this_year_ID]}\t{rouge}\t{sbert}')

            '''
            if line[2] < rouge_sim_threshold:

                print(f'HIGHLIGHT_WHOLE\t{line[0]}\t{corpus_dict[line[0].lower()]}', '|-|', 
                      f'{line[1]}\t{corpus_dict[line[1].lower()].replace("Table of Contents", "")}', '|-|', 
                      line[2], line[3], line[4], line[5])
            elif line[-1] < sbert_neg_threshold or line[-2] < lda_neg_threshold:
                print(f'{line[0]}\t{corpus_dict[line[0].lower()].replace("Table of Contents", "")}', '|-|', 
                      f'{line[1]}\t{corpus_dict[line[1].lower()].replace("Table of Contents", "")}', '|-|', 
                      line[2], line[3], line[4], line[5])
                # look-alike, rouge-2, bm25, lda, sbert

                if line[-1] < sbert_neg_threshold and line[-2] < lda_neg_threshold:
                    record.append('both')
                elif line[-1] < sbert_neg_threshold:
                    record.append('sbert')
                elif line[-2] < lda_neg_threshold:
                    record.append('lda')
    from collections import Counter
    print('statistics:')
    print(Counter(record))
    '''

if __name__ == '__main__':
    main()
