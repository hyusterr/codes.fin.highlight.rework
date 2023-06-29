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

    
def get_window(line, collections: Dict[str, str]):
    last_year_id, this_year_id, last_year_text, this_year_text = line.split('\t')

    # get context id
    last_year_id_0, last_year_id_1 = get_context_id(last_year_id)

    last_year_context_0 = collections.get(last_year_id_0, '')
    last_year_context_1 = collections.get(last_year_id_1, '')
    
    print(f'{last_year_id}\t{this_year_id}\t{last_year_context_0 + last_year_text + last_year_context_1}\t{this_year_text}')
    '''
    A0, A1, A2 = '', '', ''
    if last_year_context_0:
        A0 = f'{last_year_id_0}\t{this_year_id}\t0\t{last_year_context_0}\t{this_year_text}'
    A1 = f'{last_year_id}\t{this_year_id}\t1\t{last_year_text}\t{this_year_text}'
    if last_year_context_1:
        A2 = f'{last_year_id_1}\t{this_year_id}\t2\t{last_year_context_1}\t{this_year_text}'
    print(A0 + A1 + A2)
    '''

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
        get_window(line, corpus_dict)

if __name__ == '__main__':
    main()
