# input: a directory
# output: a probability histogram and a summary of data

import click
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
from tqdm.auto import tqdm
from multiprocessing import Pool

pd.set_option('display.float_format', lambda x: '%.4f' % x)

def read_json(filepath):
    with filepath.open('r') as f:
        data = json.load(f)
    return data

@click.command()
@click.option('--dir_name', '-d', help='input directory contains all look-alike score results')
def show_distribution(dir_name: str):
    directory = Path(dir_name)
    file_list = [p for p in directory.iterdir()]
    
    with Pool(40) as pool:
        collect_list = list(tqdm(pool.imap(read_json, file_list), total=len(file_list)))
    
    collect_list = [item for sublist in collect_list for item in sublist]
    collect_list = [item for sublist in collect_list for item in sublist]
    df = pd.DataFrame(collect_list)
    print(df.head().round(4))
    df['1-lda'] = 1 - df['lda-hellinger']
    print(df.head().round(4))
    print(df.corr())

    # df['total-score'] = df['rouge-2'] + df['bm25'] + (1 - df['lda-hellinger'])
    print(df.describe(percentiles=[.1, .2, .3, .4, .5, .6, .7, .8, .9]).round(4))
    
    '''
    plt.figure(figsize=(12, 10)) 
    plt.hist(df['rouge-2'], bins=100)
    plt.savefig('rouge-2.png')

    plt.figure(figsize=(12, 10))
    plt.hist(df['bm25'], bins=100)
    plt.savefig('bm25.png')

    plt.figure(figsize=(12, 10))
    plt.hist(df['1-lda'], bins=100)
    plt.savefig('1-lda.png')


    cm = plt.cm.get_cmap('RdBu')
    plt.figure(figsize=(12, 10))
    # definitions for the axes 
    sc = plt.scatter(df['rouge-2'], df['bm25'], c=df['1-lda'], s=0.2, cmap=cm)
    plt.xlabel('rouge-2')
    plt.ylabel('bm25')
    plt.title('look-alike score scatter plot')
    plt.colorbar(sc)
    plt.savefig(str(directory.stem) + '.png')
    '''


if __name__ == '__main__':
    show_distribution()
