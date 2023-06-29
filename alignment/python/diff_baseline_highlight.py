import re
import click
from sklearn import metrics


def generate_true_label(segment: str):
    lst = segment.split()
    label = []
    for tok in lst:
        if '*' in tok:
            label.append(1)
        else:
            label.append(0)
    return label

def generate_diff_baseline_label(last_year_seg, this_year_seg):
    lst1 = [re.sub('\W+', '', i) for i in last_year_seg.split()]
    lst2 = [re.sub('\W+', '', i) for i in this_year_seg.split()]
    pred = []
    for tok in lst2:
        if tok not in lst1:
            pred.append(1)
        else:
            pred.append(0)
    return pred

@click.command()
@click.option('--filename', '-f', help='annotation highlight one-line file')
def main(filename):
    with open(filename, 'r') as f:
        data = [i.split('\t') for i in f.read().split('\n')[:-1]]
        # 'last_year_ID   this_year_ID    last_year_segment   this_year_segment with *token*'
    
    true_labels = []
    pred_labels = []
    for d in data:
        true_label = generate_true_label(d[-1])
        pred_label = generate_diff_baseline_label(d[-2], d[-1])
        true_labels.extend(true_label)
        pred_labels.extend(pred_label)

    precision, recall, f1, support = metrics.precision_recall_fscore_support(true_labels, pred_labels)
    print('precision:\t', precision)
    print('recall:\t', recall)
    print('f1:\t', f1)


if __name__ == '__main__':
    main()
