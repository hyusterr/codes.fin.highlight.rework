import collections
from spacy.lang.en import English
import re
import json
import numpy as np

def aggregate_annotation(jsons):

    annotated_pair_ids = list(jsons[0].keys())
    if len([i for i in annotated_pair_ids if i not in jsons[0].keys()]) != 0:
        print('Inconsistent')
    if len([i for i in annotated_pair_ids if i not in jsons[1].keys()]) != 0:
        print('Inconsistent')

    aggregated_dict = collections.defaultdict(dict)

    for pair_id in annotated_pair_ids:
        keywords = collections.Counter()
        probabilities = []
        for json in jsons:
            keywords += collections.Counter(json[pair_id]['keywords'])
            W, P = map(list, list(zip(*json[pair_id]['WP'])))
            probabilities.append(P)

        # aggregation
        P_agg = np.array(probabilities).mean(axis=0).tolist()
        aggregated_dict[pair_id] = {
                'text_pair': json[pair_id]['text_pair'], 
                'keywords': [k for k, v in keywords.items() if v >= 2], 
                'WP': [(w, p) for w, p in zip(W, P_agg)]
        }

    return aggregated_dict

def read_esnli(path, class_selected=('contradiction', 'neutral', 'entailment')):
    """
    Returns:
        data_sorted: dictionary of sent pair information of a `List`.
        class_selected: string of selected class (one of above 3 classes)
    """

    # train files are split into two, need to merge before used
    import pandas as pd
    df = pd.read_csv(path)
    df.reset_index(inplace=True)
    df = df.rename(columns={
        'Sentence1': 'sentA', 'Sentence2': 'sentB',
        'Sentence1_marked_1': 'sentA_marked', 'Sentence2_marked_1': 'sentB_marked'
    })
    df = df.loc[:, ['pairID', 'gold_label', 'sentA', 'sentB', 'sentA_marked', 'sentB_marked']]
    data = collections.defaultdict(list)

    # Extract the e-snli data
    for index, row in df.iterrows():

        example = row.to_dict()
        if (example.pop('gold_label') in class_selected) and (row.isna().sum() == 0):
            data[example.pop('pairID')] = example

    # sanity check
    n_pairs = len(data)
    print(f"Total number of example: {n_pairs}")

    # sort by idb if using evaluation ser
    data_sorted = [v for k, v in sorted(data.items(), key=lambda x: x[0])]
    return data_sorted

def read_fin10k(path):
    """
    Returns:
        data_sorted: dictionary of sent pair information of a `List`.
    """
    data = collections.defaultdict(list)

    with open(path, 'r') as f:
        for i, line in enumerate(f):
            idA, idB, sentA, sentB = line.strip().split('\t')

            data[f'{idA}#{idB}'] = {
                    "idB": idB,
                    "idA": idA,
                    "sentA": sentA,
                    "sentB": sentB
            }

    # sanity check
    n_pairs = len(data)
    n_sentB = len(set([id_pair.split('#')[1] for id_pair in data.keys()]))

    print(f"Total number of example: {n_pairs}, Total number of sentB: {n_sentB} ")

    # sort by idb if using evaluation ser
    data_sorted = [v for k, v in sorted(data.items(), key=lambda x: x[0])]
    return data_sorted

def token_extraction(srcA, srcB, pair_type=2, spacy_sep=False):
    """
    Args:
        srcA, srcB: Strings of sentence pair.
        spacy_sep: separate by using `spacy tokenizer`, used when creating train data.
    """
    # normalized strings
    srcA = re.sub("\s\s+" , " ", srcA)
    srcB = re.sub("\s\s+" , " ", srcB)

    if spacy_sep:
        nlp = English()
        tokensA = [tok.text for tok in nlp(srcA)]
        tokensB = [tok.text for tok in nlp(srcB)]
    else:
        tokensA = srcA.split()
        tokensB = srcB.split()

    labelsA = [0] * len(tokensA)
    probsA = labelsA
    # we only focus on highlight sentB
    if pair_type == 2:
        labelsB = [1] * len(tokensB)
    else:
        labelsB = [pair_type] * len(tokensB)
    probsB = labelsB

    return {'type': int(pair_type),
            'sentA': srcA, 'sentB': srcB,
            'words': ["<tag1>"] + tokensA + ["<tag2>"] + tokensB + ["<tag3>"],
            'wordsA': tokensA, 'wordsB': tokensB,
            'keywordsA': [], 'keywordsB': [],
            'labels': [-1] + labelsA + [-1] + labelsB + [-1],
            'probs': [-1] + probsA + [-1] + probsB + [-1],}

def load_json(file_path, sentA=False, special_token=False, prob_threshold=0):
    out_dict = {}

    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            data = json.loads(line)
            try:
                pair_id = data.pop('idA') + "#" + data.pop('idB')
            except:
                pair_id = i

            out_dict[pair_id] = collections.defaultdict(list)

            # text pair
            out_dict[pair_id]['text_pair'] = f"# {data['sentA']}\n# {data['sentB']}"

            # keywords
            out_dict[pair_id]['keywords'] = data['keywordsB']
            if sentA: 
                out_dict[pair_id]['keywords'] += data['keywordsA']

            # words and probs
            if sentA:
                W = data['words'][1:]
                P = data['probs'][1:]
            else:
                sosB = data['probs'][1:].index(-1) + 1
                W = data['words'][sosB:]
                P = data['probs'][sosB:]

            # remove special tokens
            if special_token:
                WP = [(w_1, p_1) for (w_1, p_1) in zip(W, P)]
            else:
                WP = [(w_1, p_1) for (w_1, p_1) in zip(W, P) if p_1 != -1]

            # prob threshold
            out_dict[pair_id]['WP'] = [(w_1, p_1) if (p_1 < 0 or p_1 > prob_threshold) \
                    else (w_1, 0) for (w_1, p_1) in WP]

    return out_dict

def load_truth(file_path, sentA=True):
    truth = {}

    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            data = json.loads(line)
            try:
                pair_id = data['idA'] + "#" + data['idB']
            except:
                pair_id = i

            truth[pair_id] = {
                    "labels": data['labels'], 
                    "keywords": data['keywordsB'], 
                    "text_pair": f"# {data['sentA']}\n# {data['sentB']}"
            }

    return truth

def load_pred(file_path, special_token=False, prob_threshold=0):
    prediction = {}
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            data = json.loads(line)
            try:
                pair_id = data.pop('idA') + "#" + data.pop('idB')
            except:
                pair_id = i

            prediction[pair_id] = []

            flag = False
            for j, (w, p) in enumerate(zip(data['words'], data['probs'])):

                if p == -1:
                    # when aggregation
                    if special_token:
                        prediction[pair_id].append( (w, p) )
                        flag = True
                    # when evalaution
                    else:
                        flag = False if j == 0 else True
                elif flag:
                    if p >= prob_threshold:
                        prediction[pair_id].append( (w, p) )
                    else:
                        prediction[pair_id].append( (w, 0) )
                else:
                    pass

    return prediction

def fleiss_kappa(table, method='fleiss'):
    """Fleiss' and Randolph's kappa multi-rater agreement measure

    Parameters
    ----------
    table : array_like, 2-D
        assumes subjects in rows, and categories in columns. Convert raw data
        into this format by using
        :func:`statsmodels.stats.inter_rater.aggregate_raters`
    method : str
        Method 'fleiss' returns Fleiss' kappa which uses the sample margin
        to define the chance outcome.
        Method 'randolph' or 'uniform' (only first 4 letters are needed)
        returns Randolph's (2005) multirater kappa which assumes a uniform
        distribution of the categories to define the chance outcome.

    Returns
    -------
    kappa : float
        Fleiss's or Randolph's kappa statistic for inter rater agreement

    Notes
    -----
    no variance or hypothesis tests yet

    Interrater agreement measures like Fleiss's kappa measure agreement relative
    to chance agreement. Different authors have proposed ways of defining
    these chance agreements. Fleiss' is based on the marginal sample distribution
    of categories, while Randolph uses a uniform distribution of categories as
    benchmark. Warrens (2010) showed that Randolph's kappa is always larger or
    equal to Fleiss' kappa. Under some commonly observed condition, Fleiss' and
    Randolph's kappa provide lower and upper bounds for two similar kappa_like
    measures by Light (1971) and Hubert (1977).

    References
    ----------
    Wikipedia https://en.wikipedia.org/wiki/Fleiss%27_kappa

    Fleiss, Joseph L. 1971. "Measuring Nominal Scale Agreement among Many
    Raters." Psychological Bulletin 76 (5): 378-82.
    https://doi.org/10.1037/h0031619.

    Randolph, Justus J. 2005 "Free-Marginal Multirater Kappa (multirater
    K [free]): An Alternative to Fleiss' Fixed-Marginal Multirater Kappa."
    Presented at the Joensuu Learning and Instruction Symposium, vol. 2005
    https://eric.ed.gov/?id=ED490661

    Warrens, Matthijs J. 2010. "Inequalities between Multi-Rater Kappas."
    Advances in Data Analysis and Classification 4 (4): 271-86.
    https://doi.org/10.1007/s11634-010-0073-4.
    """

    table = 1.0 * np.asarray(table)   #avoid integer division
    n_sub, n_cat =  table.shape
    n_total = table.sum()
    n_rater = table.sum(1)
    n_rat = n_rater.max()
    #assume fully ranked
    assert n_total == n_sub * n_rat

    #marginal frequency  of categories
    p_cat = table.sum(0) / n_total

    table2 = table * table
    p_rat = (table2.sum(1) - n_rat) / (n_rat * (n_rat - 1.))
    p_mean = p_rat.mean()

    if method == 'fleiss':
        p_mean_exp = (p_cat*p_cat).sum()
    elif method.startswith('rand') or method.startswith('unif'):
        p_mean_exp = 1 / n_cat

    kappa = (p_mean - p_mean_exp) / (1- p_mean_exp)
    return kappa

def aggregate_raters(data, n_cat=None):
    '''convert raw data with shape (subject, rater) to (subject, cat_counts)

    brings data into correct format for fleiss_kappa

    bincount will raise exception if data cannot be converted to integer.

    Parameters
    ----------
    data : array_like, 2-Dim
        data containing category assignment with subjects in rows and raters
        in columns.
    n_cat : None or int
        If None, then the data is converted to integer categories,
        0,1,2,...,n_cat-1. Because of the relabeling only category levels
        with non-zero counts are included.
        If this is an integer, then the category levels in the data are already
        assumed to be in integers, 0,1,2,...,n_cat-1. In this case, the
        returned array may contain columns with zero count, if no subject
        has been categorized with this level.

    Returns
    -------
    arr : nd_array, (n_rows, n_cat)
        Contains counts of raters that assigned a category level to individuals.
        Subjects are in rows, category levels in columns.
    categories : nd_array, (n_category_levels,)
        Contains the category levels.

    '''
    data = np.asarray(data)
    n_rows = data.shape[0]
    if n_cat is None:
        #I could add int conversion (reverse_index) to np.unique
        cat_uni, cat_int = np.unique(data.ravel(), return_inverse=True)
        n_cat = len(cat_uni)
        data_ = cat_int.reshape(data.shape)
    else:
        cat_uni = np.arange(n_cat)  #for return only, assumed cat levels
        data_ = data

    tt = np.zeros((n_rows, n_cat), int)
    for idx, row in enumerate(data_):
        ro = np.bincount(row)
        tt[idx, :len(ro)] = ro

    return tt, cat_uni
