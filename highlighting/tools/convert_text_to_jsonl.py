import re
import os
import json
import string
import spacy
import random
import argparse
import numpy as np
from nltk.corpus import stopwords
from collections import defaultdict
from spacy.lang.en import English
from utils import read_esnli, read_fin10k, token_extraction

def convert_to_bert(args, data):

    f = open(args.path_output_file, 'w')
    for i, example in enumerate(data):
        example_info = token_extraction(
                example['sentA'].strip(), 
                example['sentB'].strip(),
                pair_type=args.fin10k_type,
                spacy_sep=args.use_spacy_sep,
        )
        example.update(example_info)
        # if annotation
        f.write(json.dumps(example) + '\n')
    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # For all data
    parser.add_argument("-input", "--path_input_file", type=str)
    parser.add_argument("-output", "--path_output_file", type=str)
    parser.add_argument("-type", "--fin10k_type", type=int, default=-1)
    parser.add_argument("-spacy_sep", "--use_spacy_sep", action='store_true', default=False)
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.path_output_file), exist_ok=True)

    if 'esnli' in args.path_input_file:
        # so far, we use 'contradiction' pair
        data = read_esnli(args.path_input_file, ("contradiction"))
        convert_to_bert(args, data)
    else:
    # if 'fin10k' in args.path_input_file:
        data = read_fin10k(args.path_input_file)
        convert_to_bert(args, data)


    print("Done")
