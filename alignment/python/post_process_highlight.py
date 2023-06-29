import sys
import json


with open(sys.argv[1]) as f:
    data = [json.loads(l) for l in f.readlines()]

for d in data:
    labels = d['label']
    words = d['word']
    labels = labels[:len(words)]

    for label, word in zip(labels, words):
        if label == 1:
            print(f'*{word}*', end=' ')
        else:
            print(word, end=' ')
        
    print('\n')

