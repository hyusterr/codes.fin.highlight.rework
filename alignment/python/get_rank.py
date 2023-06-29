import sys
import pandas as pd

with open(sys.argv[1], 'r') as f:
    data = f.read().split('\n')[:-1]
data = pd.DataFrame([d.split('\t') for d in data])
columns = ['last_year_id', 'this_year_id', 'last_year_text', 'this_year_text', 'rouge', 'sbert']
data.columns = columns
data['rouge'] = data['rouge'].map(float)
data['sbert'] = data['sbert'].map(float)

gb = data.groupby('this_year_id')
print('total aligned:', len(data))
print('total groups:', len(gb.groups))
# print(gb.get_group('844161_17_item7_p124_s0'))

for name, group in gb:
    tmp = group.sort_values('sbert')
    # print(tmp.to_csv(sep='\t', header=False, index=False, line_terminator='\n'))
    if len(tmp) > 1:
        out = tmp[columns[:-2]].to_csv(sep='\t', header=False, index=False, line_terminator='\n').strip().split('\n')
        i = 0
        for o in out:
            pass
            # print(o)
        
