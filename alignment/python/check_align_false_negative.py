import sys

with open(sys.argv[1], 'r') as f:
    data = [i.split('\t') for i in f.read().split('\n')[:-1]]

for i in data:
    if i[-1] != i[-2]:
        print(i)
