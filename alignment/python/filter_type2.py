#!usr/bin/python3
# encoding: utf-8

import click
from typing import Dict
from tqdm.auto import tqdm
'''
DATA FORMAT:
1138118_12_item7_p113_s0        1138118_13_item7_p115_s1        (6) Due to the nature of guarantees, payments could be due at any time upon the occurrence of certain triggering events including default.      Due to the nature of this item, payments could be due at any time upon the occurrence of certain events.
'''

def get_context_id(text_ID: str):
    id_list = text_ID.split('_')
    prefix = '_'.join(id_list[:-1]) + '_'
    sid = id_list[-1]
    sid_0 = f's{int(sid[1:]) - 1}'
    sid_1 = f's{int(sid[1:]) + 1}'
    # if not exist: use try and error in collection to catch
    return prefix + sid_0, prefix + sid_1

    
def filter_one_contain_the_other(line, collections: Dict[str, str]):
    last_year_id, this_year_id, last_year_text, this_year_text, rouge, sbert = line.split('\t')

    # case1: not one contains in the other
    # case2: A contains in B
    #   check if context is also same --> if not also print
    if this_year_text not in last_year_text and last_year_text not in this_year_text:
        print(f'{last_year_id}\t{this_year_id}\t{last_year_text}\t{this_year_text}')
    else:
        # get context id
        last_year_id_0, last_year_id_1 = get_context_id(last_year_id)
        this_year_id_0, this_year_id_1 = get_context_id(this_year_id)

        last_year_context_0 = collections.get(last_year_id_0, '')
        last_year_context_1 = collections.get(last_year_id_1, '')
        last_year_context = last_year_context_0 + last_year_text + last_year_context_1

        this_year_context_0 = collections.get(this_year_id_0, '')
        this_year_context_1 = collections.get(this_year_id_1, '')
        this_year_context = this_year_context_0 + this_year_text + this_year_context_1
        
        if this_year_context not in last_year_context and this_year_context not in last_year_context:
            # DIFF_CONTEXT
            print(f'{last_year_id}\t{this_year_id}\t{last_year_context}\t{this_year_context}')#\t{rouge}\t{sbert}')
        else:
            # TYPE1_ERROR
            # print(f'TYPE1_ERROR\t{line}')
            pass


@click.command()
@click.option('--corpus', '-c', help='{cross-seg, sentence}-collection.txt')
@click.option('--type2_raw', '-t', help='type2 files before filter')
def main(corpus, type2_raw):
    
    # prepare collection
    corpus_dict = dict()
    with open(corpus) as f:
        for line in tqdm(f):
            try:
                idx, sentence = line.split('\t')
                corpus_dict[idx.lower()] = sentence.strip()
            except ValueError:
                pass

    with open(type2_raw) as f:
        data = f.read().split('\n')[:-1]
    
    for line in data:
        filter_one_contain_the_other(line, corpus_dict)

if __name__ == '__main__':
    main()
