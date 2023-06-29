import sys

with open(sys.argv[1], 'r') as f:
    data = f.read().split('=' * 80)[:-1]

with open(sys.argv[2], 'r') as f: # topk file
    tmp = f.read().split('\n')[:-1]
collections = dict()
for t in tmp:
    index = t.split('\t')[1]
    if index in collections:
        collections[index].append(t)
    else:
        collections[index] = [t]

for di in data:
    d = di.strip().split('\n')
    last_year_text, this_year_text = d[1], d[2]
    prefix = d[0].split()
    last_year_id, this_year_id = prefix[0], prefix[1]
    
    try:
        for l in collections[this_year_id]:
            id1, id2, text1, text2 = l.split('\t')
            if id1 != last_year_id:
                print(f'{id1} {id2}')
                print(text1)
                print(text2)
                print()
                print('=' * 80)
            else:
                print(di.strip())
                print()
                print('=' * 80)
    except KeyError:
        print(di.strip())
        print()
        print('=' * 80)

    # if 'CLASS1' in prefix:
    #     print(f'{last_year_id}\t{this_year_id}\t{last_year_text}\t{this_year_text}')
