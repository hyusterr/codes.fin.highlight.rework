import sys

with open(sys.argv[1], 'r') as f:
    data = f.read().split('=' * 80)[:-1]

for di in data:
    d = di.strip().split('\n')
    last_year_text, this_year_text = d[1], d[2]
    prefix = d[0].split()
    last_year_id, this_year_id = prefix[0], prefix[1]
    # print(f'{last_year_id}\t{this_year_id}\t{last_year_text}\t{this_year_text}')

    if 'CLASS1' in prefix or 'class1' in prefix:
        print(f'{last_year_id}\t{this_year_id}\t{last_year_text}\t{this_year_text}')
