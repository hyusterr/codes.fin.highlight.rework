import click


@click.command()
@click.option('--exist_eval_file', '-e')
@click.option('--new_shuf_file', '-n')
def pick_eval_train(exist_eval_file, new_shuf_file):
    with open(exist_eval_file, 'r') as f:
        data = [l.split('\t') for l in f.read().split('\n')[:-1]]
        assert len(data) == 180
    exist_eval_ids = ['\t'.join(l[:2]) for l in data]

    with open(new_shuf_file, 'r') as f:
        new_data = f.read().split('\n')[:-1]
    for l in new_data:
        id_pair = '\t'.join(l.split('\t')[:2])
        if id_pair not in exist_eval_ids:
            print(l)

if __name__ == '__main__':
    pick_eval_train()
