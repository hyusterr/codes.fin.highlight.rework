import os
import ndjson
import json
import click
from tqdm.auto import tqdm

# 0.5568      0.7536
@click.command()
@click.option('--directory', '-d', help='directory contain files after get-sbert-cossim')
@click.option('--corpus', '-c', help='pool contain all INDEX<TAB>segments')
@click.option('--rouge_sim_threshold', '-rs', type=float, default=0.6296)
@click.option('--rouge_sim_hard_threshold', '-rhs', type=float, default=0.1633)
def main(directory, corpus, rouge_sim_threshold, rouge_sim_hard_threshold):
    
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

            if rouge_sim_hard_threshold < rouge <= rouge_sim_threshold: 
                print(f'TYPE_1\t{last_year_ID}\t{this_year_ID}\t{corpus_dict[last_year_ID]}\t{corpus_dict[this_year_ID]}')
            elif rouge <= rouge_sim_hard_threshold:
                print(f'TYPE_HARD1\t{last_year_ID}\t{this_year_ID}\t{corpus_dict[last_year_ID]}\t{corpus_dict[this_year_ID]}')

if __name__ == '__main__':
    main()
