# input: a directory
# output: a probability histogram and a summary of data

import click
import json
import ndjson
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
from tqdm.auto import tqdm
from multiprocessing import Pool

pd.set_option('display.float_format', lambda x: '%.4f' % x)

def read_json(filepath):
    with filepath.open('r') as f:
        data = [json.loads(jline) for jline in f.read().splitlines()]
    return data

@click.command()
@click.option('--dir_name', '-d', help='input directory contains all sbert score results')
def show_distribution(dir_name: str):
    directory = Path(dir_name)
    file_list = [p for p in directory.iterdir()]
    new_directory = Path('./results/cross-seg/sort_by_rouge/sbert_top1_missing/')
    
    with Pool(40) as pool:
        collect_list = list(tqdm(pool.imap(read_json, file_list), total=len(file_list)))
    
    data_list = []
    for file_name, data in tqdm(zip(file_list, collect_list)):
        tmp_set = set()
        list_to_write = []
        for d in data:
            this_year_id = d[0]
            if this_year_id not in tmp_set:
                data_list.append(d[2:])
                tmp_set.add(this_year_id)
                list_to_write.append(d)
        new_file_path = new_directory / file_name.name
        with open(new_file_path, 'w') as f:
            ndjson.dump(list_to_write, f)

    
    # data looks like:
    # ["1006281_18_ITEM7_P0_S0", "1006281_17_ITEM7_P0_S0", 1.0, 78.3867, 1.0, 1.0]
    # collect_list = [item[2:] for sublist in collect_list for item in sublist]
    
    '''
    df = pd.DataFrame(data_list)
    df.columns = ['rouge-2', 'bm25', '1-lda', 'sbert']
    print(df.head().round(4))
    print(df.corr())

    # df['total-score'] = df['rouge-2'] + df['bm25'] + (1 - df['lda-hellinger'])
    print(df.describe(percentiles=[.1, .2, .3, .4, .5, .6, .7, .8, .9]).round(4))
    
    plt.figure(figsize=(12, 10)) 
    plt.hist(df['rouge-2'], bins=100)
    plt.savefig('select-rouge-2.png')

    plt.figure(figsize=(12, 10))
    plt.hist(df['bm25'], bins=100)
    plt.savefig('select-bm25.png')

    plt.figure(figsize=(12, 10))
    plt.hist(df['1-lda'], bins=100)
    plt.savefig('select-1-lda.png')

    plt.figure(figsize=(12, 10))
    plt.hist(df['sbert'], bins=100)
    plt.savefig('select-sbert.png')


    cm = plt.cm.get_cmap('RdBu')
    plt.figure(figsize=(12, 10))
    # definitions for the axes 
    sc = plt.scatter(df['rouge-2'], df['bm25'], c=df['1-lda'], s=0.2, cmap=cm)
    plt.xlabel('rouge-2')
    plt.ylabel('bm25')
    plt.title('select look-alike score scatter plot')
    plt.colorbar(sc)
    plt.savefig('select-scatter-' + str(directory.stem) + '.png')
    '''


if __name__ == '__main__':
    show_distribution()
