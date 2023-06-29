import sys

with open(sys.argv[1], 'r') as f:
    train_data = f.read().split('\n')

with open(sys.argv[2], 'r') as f:
    eval_data = f.read().split('\n')

eval_IDs = ['\t'.join(e.split('\t')[:2]) for e in eval_data]
for t in train_data:
    train_id = '\t'.join(t.split('\t')[:2])
    if train_id not in eval_IDs:
        print(t)
