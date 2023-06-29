# import warnings
# warnings.filterwarnings("ignore")
import logging
logging.disable(logging.INFO)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

import json
import ndjson
import click
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2', device='cuda')
def get_sbert_cos_sim(sentence_pair1, sentence_pair2, model=model):
    
    embeddings1 = model.encode(sentence_pair1, convert_to_tensor=True)
    embeddings2 = model.encode(sentence_pair2, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

    return [round(cosine_scores[i][i].item(), 4) for i in range(len(sentence_pair1))]


@click.command()
@click.option('--corpus_name', '-c', help='collections contain a pool of INDEX<TAB>Segments')
@click.option('--json_name', '-j', help='lda-bm25-rouge record .json file after max-diff-drop')
@click.option('--out_json_name', '-o', help='.json filename for saving cos sim results')
def main(corpus_name, json_name, out_json_name):
    
    with open(corpus_name, 'r') as f:
        segments = [i.strip() for i in f.readlines()]
        dataset = {s.split('\t')[0]: s.split('\t')[1] for s in segments if len(s.split('\t')) == 2}
        # 1001082_12_item12_s1: some sentences

    with open(json_name, 'r') as f:
        alignment_results = json.load(f)
        # year_t: {year_t-1, rouge-l} # already sorted by ROUGE

    # get sentences pair # (sent1, sent2_id, rouge)
    # only use the all rouge-l sentences after max diff drop

    sentence_data = []
    for k, v in alignment_results.items():
        for i in range(len(v)):
            sentence_data.append([k, 
                                  v[i]['last-year-id'], 
                                  round(v[i]['rouge-2'], 4), 
                                  round(v[i]['bm25'], 4), 
                                  round(v[i]['lda'], 4)
                                  ])

    sentence_pair1 = [dataset[v[0]] for v in sentence_data]
    sentence_pair2 = [dataset[v[1]] for v in sentence_data]
    cosine_scores = get_sbert_cos_sim(sentence_pair1, sentence_pair2)
    # last-year-id, rouge-2, bm25, lda, sbert
    for i in range(len(sentence_data)):
        sentence_data[i].append(cosine_scores[i]) 

    with open(out_json_name, 'w') as f:
        ndjson.dump(sentence_data, f)


if __name__ == '__main__':
    main()
