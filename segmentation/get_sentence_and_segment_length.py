import argparse
import pandas as pd
from tqdm import tqdm
from transformers import BertTokenizer, BertModel

parser = argparse.ArgumentParser()
parser.add_argument('--collection')
parser.add_argument('--output_dir')
args = parser.parse_args()

from tqdm import tqdm
import pandas as pd
from transformers import BertTokenizer, BertModel

def read_collections(file):
    data = dict()
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            fullID, sentence = line.split('\t')
            data[fullID] = sentence
        f.close()

    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.reset_index()
    df.columns = ['fullID', 'sentence']

    return data, df

def get_num_of_seg(df):
    df1 = df['fullID'].str.split('_', expand=True)
    last_pid_indexes = [idx-1 for idx in df1[(df1[3]=='P0') & (df1[4]=='S0')].index][1:]
    li = df1.loc[last_pid_indexes, 3].str.replace('P', '').astype('int')
    last_para = int(df1.iloc[-1][3].replace('P', '')) # last
    return (sum(li)+last_para) / 800

def len_sent(tokenizer, text):
    return len(tokenizer.tokenize(text))

def get_sentence_length(df, tokenizer):
    df1 = df.copy()
    lengths = []
    for sent in tqdm(list(df1['sentence'])):
        lengths.append(len_sent(tokenizer, sent))
    df1['sent_length'] = lengths
    return df1

def get_segment_length(df):
    # create column: positioin
    # input already calculated sentence length df
    df1 = df.copy()
    df1['position'] = ['']*len(df)

    cur_pid = 0
    pos = 0
    positions = []
    for fullID in list(df['fullID']):
        cik, year, item, pid, sid = fullID.split('_')
        pid = int(pid.replace('P', ''))
        if cur_pid!=pid:
            pos+=1
            cur_pid = pid
        positions.append(pos)
    df1['position'] = positions
    
    df1['segment_length'] = [0]*len(df) # reset 0
    for pos in tqdm(positions):
        df3 = df1[df1['position']==pos]
        seg_length = sum(df3['sent_length'])
        df1.loc[df3.index, 'segment_length'] = seg_length
        # seg = " ".join([data[fullID] for fullID in df3.fullID])
        # df1.loc[df3.index, 'segment_length'] = len_sent(tokenizer, seg)
    
    return df1, positions

def main(args):
    """
    input collection
    return sentence and segment level segment length
    print number of long sentences, long sentence id, length
    print average segment length, average sentence length
    """
    file = args.collection
    output_dir = args.output_dir
    data, df = read_collections(file)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    df_sent = get_sentence_length(df, tokenizer)
    df_seg, positions = get_segment_length(df_sent)
    df_seg[['sent_length', 'position', 'segment_length']].to_csv(f'{output_dir}/sentence_and_segment_length.csv', index=False)
    print('Done')

if __name__ == '__main__':
    main(args)