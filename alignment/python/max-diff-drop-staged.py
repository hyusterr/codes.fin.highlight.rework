import json
import click
from typing import List, Dict

'''
{"sentenceID": [{"last-year-id": "sentenceID", "rouge-l": float},...}
'''


def get_sub_sequence(lst: List[dict]) -> List[dict]:
    
    lst = sorted(lst, key=lambda x: x['rouge-2'], reverse=True)
    
    rouges = [i['rouge-2'] for i in lst]
    rouge_diffs = [abs(rouges[i] - rouges[i - 1]) for i in range(1, len(rouges))]
    rouge_max_diff = max(rouge_diffs)
    
    output = [lst[0]]
    for i in range(1, len(rouges)):
        if rouge_diffs[i - 1] < rouge_max_diff:
            output.append(lst[i])
        else:
            break
    
    return output


@click.command()
@click.option('--filename', '-f', help='JSON file contains top10 lda-bm25-rouge score')
@click.option('--output', '-o', help='file to write the result')
def main(filename, output):
    
    with open(filename, 'r') as f:
        data = json.load(f)

    for sentID, lst_of_dict in data.items():
        lst_of_dict = get_sub_sequence(lst_of_dict)
        data[sentID] = lst_of_dict

    with open(output, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
