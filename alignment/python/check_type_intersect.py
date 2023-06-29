from itertools import combinations

TYPES =  ['TYPE_0', 'TYPE_1', 'TYPE_2']
set_dict = dict()
for type_ in TYPES:
    with open(f'{type_}.uniqID', 'r') as f:
        set_dict[type_] = set(f.read().split('\n')[:-1])

for t1, t2 in combinations(TYPES, 2):
    print(t1, t2, 'intersects:')
    print(len(set_dict[t1].intersection(set_dict[t2])))
        
