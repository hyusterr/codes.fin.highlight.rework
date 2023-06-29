import sys

with open(sys.argv[1], 'r') as f:
    data = [l.split('\t') for l in f.readlines()]

for d in data:
    print('\t'.join(d[1:]))
    '''
    print(d[1], d[2])
    print(d[3])
    print(d[4])
    print('=' * 80)
    '''

