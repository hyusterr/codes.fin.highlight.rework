import pickle
from collections import defaultdict
rp = defaultdict(list)

rp['esnli-zs-highlighter'] = [
1.0                        
, 0.5                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.75                        
, 1.0                        
, 1.0                        
, 0.5                        
, 0.8571428571428571                        
, 0.5                        
, 0.5                        
, 0.8571428571428571                        
, 0.8                        
, 0.5                        
, 0.75                        
, 0.75                        
, 1.0                        
, 1.0                        
, 0.6666666666666666                        
, 0.6923076923076923                        
, 0.5                        
, 0.5                        
, 1.0                        
, 0.6086956521739131                        
, 0.6666666666666666                        
, 0.75                        
, 1.0                        
, 0.75                        
, 0.8333333333333334                        
, 1.0                        
, 0.0                        
, 0.75                        
, 0.5                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.7142857142857143                        
, 1.0                        
, 1.0                        
, 0.6666666666666666                        
, 0.75                        
, 0.3333333333333333                        
, 1.0                        
, 1.0                        
, 0.0                        
, 1.0                        
, 0.8                        
, 0.8571428571428571                        
, 0                        
, 1.0                        
, 1.0                        
, 0.8                        
, 0.75                        
, 1.0                        
, 0.5333333333333333                        
, 0.875                        
, 0.8571428571428571                        
, 0.7777777777777778                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.8571428571428571                        
, 0.3333333333333333                        
, 0.5833333333333334                        
, 0.6666666666666666                        
, 0.7857142857142857                        
, 0.6666666666666666                        
, 0                        
, 0.7692307692307693                        
, 0.2                        
, 0.5                        
, 1.0                        
, 1.0                        
, 0.8                        
, 0.8                        
, 0.75                        
, 1.0                        
, 1.0                        
, 0.7692307692307693                        
, 1.0                        
, 1.0                        
, 0.5                        
, 0.6                        
, 1.0                        
, 0.5                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.25                        
, 1.0                        
, 1.0                        
, 0.6666666666666666                        
, 1.0                        
, 1.0                        
, 0.8333333333333334                        
, 0.8571428571428571                        
, 0.875                        
, 1.0                        
, 1.0                        
, 0.6                        
, 0.6                        
, 0.4444444444444444                        
, 0.2857142857142857                        
, 0.7142857142857143                        
, 1.0                        
, 1.0                        
, 0.8                        
, 0.5                        
, 1.0                        
, 0.8                        
, 0.5833333333333334                        
, 1.0                        
, 1.0                        
, 0.5                        
, 1.0                        
, 1.0                        
, 0.5                        
, 0.4444444444444444                        
, 0.5555555555555556                        
, 0.0                        
, 0.5384615384615384                        
, 1.0                        
, 0.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.5882352941176471                        
, 0.8571428571428571                        
, 0.5                        
, 0.6                        
, 0.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.6                        
, 0.8                        
, 1.0                        
, 0.8461538461538461                        
, 1.0                        
, 0.75                        
, 1.0                        
, 0.625                        
, 1.0                        
, 0.6666666666666666                        
, 0.8333333333333334                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.6                        
, 1.0                        
, 0.75                        
, 0.5                        
, 0.5                        
, 1.0                        
, 0.5                        
, 1.0                        
, 1.0                        
, 0.7777777777777778                        
, 1.0                        
, 0.6666666666666666                        
, 0.75                        
, 1.0                        
, 0.8076923076923077                        
, 0.6470588235294118                        
, 0.0                        
, 0.6                        
, 1.0                        
, 0.7142857142857143                        
, 1.0                        
, 0.4166666666666667                        
, 0.3333333333333333                        
, 0.0                        
, 0.5                        
, 0.3333333333333333                        
, 0.6666666666666666                        
, 0.2857142857142857                        
, 1.0                        
, 0.6666666666666666                        
, 0.6                        
, 1.0                        
, 0.42857142857142855                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.6428571428571429                        
, 1.0                        
, 0.6666666666666666                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.7142857142857143                        
, 0                        
, 0.7941176470588235                        
, 0.6363636363636364                        
, 0.9411764705882353                        
, 1.0                        
, 0.8333333333333334                        
, 1.0                        
, 0.7857142857142857                        
, 0.6                        
, 0.7142857142857143                        
, 1.0                        
, 0.9090909090909091                        
, 1.0                        
, 0.7096774193548387                        
, 0.875                        
, 0.7                        
, 0.8571428571428571                        
, 1.0                        
, 1.0                        
, 0.5714285714285714                        
, 0.7777777777777778                        
, 1.0                        
, 0.5294117647058824                        
, 0.8235294117647058                        
, 0.8666666666666667                        
, 0.7142857142857143                        
, 0.8076923076923077                        
, 0.8888888888888888                        
, 0.6666666666666666                        
, 0.875                        
, 1.0                        
, 0.7692307692307693                        
, 1.0                        
, 0.0                        
, 0.6666666666666666                        
, 0.8                        
, 0.7142857142857143                        
, 0.38461538461538464                        
, 0.5                        
, 0.4166666666666667                        
, 0.7777777777777778                        
, 0.7777777777777778                        
, 0.3333333333333333                        
, 0.6666666666666666                        
, 0.7                        
, 0.7272727272727273                        
, 0.0                        
, 0.5                        
, 0.75                        
, 0                        
, 0.7272727272727273                        
, 0.8181818181818182                        
, 0.6666666666666666                        
, 0.8888888888888888                        
, 0                        
, 0.7857142857142857                        
, 0.6956521739130435                        
, 0.75                        
, 0.6666666666666666                        
, 0.8                        
, 0.75                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.75                        
, 0.5                        
, 0.6538461538461539                        
, 0.6666666666666666                        
, 0.5                        
, 0.5                        
, 0.4                        
, 0.6666666666666666                        
, 0.5                        
, 0.75                        
, 0.6666666666666666                        
, 0.8                        
, 0.9024390243902439                        
, 0.6363636363636364                        
, 1.0                        
, 0.7619047619047619                        
, 1.0                        
, 0.8                        
, 0.5                        
, 1.0                        
, 0.6666666666666666                        
, 0.75                        
, 0.3684210526315789                        
, 0.36363636363636365                        
, 1.0                        
, 0.9090909090909091                        
, 1.0                        
, 0.7272727272727273                        
, 0.6                        
, 0.5                        
, 0.8636363636363636                        
, 0.8461538461538461                        
, 0.6666666666666666                        
, 1.0                        
, 0.4                        
, 0.6190476190476191                        
, 0.8125                        
, 0.6                        
, 0.6666666666666666                        
, 0.6666666666666666                        
, 0.7857142857142857                        
, 0.8461538461538461                        
, 0.5555555555555556                        
, 0.5294117647058824                        
, 0.7142857142857143                        
, 0.875                        
, 0.8571428571428571                        
, 0.6666666666666666                        
, 0.6666666666666666                        
, 0.6666666666666666                        
, 1.0                        
, 0.8333333333333334                        
, 0.0                        
, 0.7692307692307693                        
, 1.0                        
, 0.7777777777777778                        
, 0.7272727272727273                        
, 0.47058823529411764                        
, 0.7                        
, 0.9130434782608695                        
, 0.8888888888888888                        
, 0.6                        
, 1.0                        
, 0.5                        
, 0.4166666666666667                        
, 0.7333333333333333                        
, 0.75                        
, 0.5555555555555556                        
, 0.7777777777777778                        
, 0.7272727272727273                        
, 0.7222222222222222                        
, 0.8666666666666667                        
, 0.8571428571428571                        
, 0.625                        
, 0.75                        
, 0.75                        
, 0.7333333333333333                        
, 0.5                        
, 0.8421052631578947                        
, 0.7272727272727273                        
, 0.8                        
, 0.875                        
, 0.6923076923076923                        
, 0.8333333333333334                        
, 0.8888888888888888                        
, 0.875                        
, 1.0                        
, 0.6956521739130435                        
, 0.6666666666666666                        
, 0.6153846153846154                        
, 0.6666666666666666                        
, 0.6470588235294118                        
, 0.7142857142857143                        
, 1.0                        
, 0.6666666666666666                        
, 0.75                        
, 0.7272727272727273                        
, 1.0                        
, 0.5909090909090909                        
, 0.75                        
, 0.8888888888888888                        
, 0.8                        
, 0.8461538461538461                        
, 0.7272727272727273                        
, 0.5714285714285714                        
, 0.7142857142857143                        
, 0.5                        
, 0.75                        
, 0.6666666666666666                        
, 0.14285714285714285                        
, 1.0                        
, 0.5555555555555556                        
, 0.75                        
, 0                        
, 0.6666666666666666                        
, 0.5                        
, 0.5714285714285714                        
, 1.0                        
, 0.8461538461538461                        
, 0.631578947368421                        
, 0.3333333333333333                        
, 0.4                        
, 0.5333333333333333                        
, 1.0                        
, 1.0                        
, 0.6666666666666666                        
, 0.6                        
, 0.42857142857142855                        
, 0.5714285714285714                        
, 0.5                        
, 0.6666666666666666                        
, 0.0                        
, 0.75                        
, 0.5                        
, 0.8461538461538461                        
,]
rp['further-finetune-sl-smooth-2'] = [
1.0                        
, 0.625                        
, 1.0                        
, 0.5                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.75                        
, 1.0                        
, 0.0                        
, 0.6666666666666666                        
, 0.8571428571428571                        
, 0.5                        
, 0.5                        
, 0.8571428571428571                        
, 0.8                        
, 0.5                        
, 0.75                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.6666666666666666                        
, 0.8461538461538461                        
, 0.75                        
, 1.0                        
, 1.0                        
, 0.8260869565217391                        
, 0.6666666666666666                        
, 0.75                        
, 1.0                        
, 0.75                        
, 0.6666666666666666                        
, 1.0                        
, 0.5                        
, 0.875                        
, 0.5                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.7857142857142857                        
, 1.0                        
, 1.0                        
, 0.6666666666666666                        
, 0.75                        
, 0.6666666666666666                        
, 0.5                        
, 1.0                        
, 0.0                        
, 1.0                        
, 0.8                        
, 0.8571428571428571                        
, 0                        
, 1.0                        
, 1.0                        
, 0.8                        
, 0.75                        
, 1.0                        
, 0.5333333333333333                        
, 0.875                        
, 1.0                        
, 0.7777777777777778                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.7142857142857143                        
, 0.3333333333333333                        
, 0.8333333333333334                        
, 0.6666666666666666                        
, 0.7142857142857143                        
, 0.6666666666666666                        
, 0                        
, 0.8461538461538461                        
, 0.6                        
, 0.5                        
, 1.0                        
, 1.0                        
, 0.8                        
, 0.8                        
, 0.875                        
, 1.0                        
, 1.0                        
, 0.6923076923076923                        
, 1.0                        
, 1.0                        
, 0.5                        
, 0.8                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.8333333333333334                        
, 0.5                        
, 1.0                        
, 0.6666666666666666                        
, 0.6666666666666666                        
, 1.0                        
, 1.0                        
, 0.8333333333333334                        
, 0.8571428571428571                        
, 0.875                        
, 1.0                        
, 1.0                        
, 0.6                        
, 0.6                        
, 0.7777777777777778                        
, 0.5714285714285714                        
, 0.8571428571428571                        
, 0.6666666666666666                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.8                        
, 0.6666666666666666                        
, 1.0                        
, 1.0                        
, 0.6666666666666666                        
, 1.0                        
, 1.0                        
, 0.5                        
, 0.4444444444444444                        
, 0.5555555555555556                        
, 0.5                        
, 0.6153846153846154                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.7647058823529411                        
, 0.8571428571428571                        
, 0.5                        
, 0.6                        
, 0.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.6                        
, 0.9333333333333333                        
, 1.0                        
, 0.8461538461538461                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.875                        
, 1.0                        
, 0.6666666666666666                        
, 0.8333333333333334                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.8                        
, 1.0                        
, 0.75                        
, 0.5                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.6666666666666666                        
, 1.0                        
, 1.0                        
, 0.8076923076923077                        
, 0.7058823529411765                        
, 0.0                        
, 0.8                        
, 1.0                        
, 0.7714285714285715                        
, 0.7142857142857143                        
, 0.6666666666666666                        
, 0.3333333333333333                        
, 0.25                        
, 1.0                        
, 0.3333333333333333                        
, 0.7777777777777778                        
, 0.42857142857142855                        
, 0.8                        
, 0.6666666666666666                        
, 0.9                        
, 1.0                        
, 0.8571428571428571                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.6428571428571429                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 1.0                        
, 0.9047619047619048                        
, 0                        
, 0.8529411764705882                        
, 0.8181818181818182                        
, 0.8235294117647058                        
, 1.0                        
, 0.6666666666666666                        
, 1.0                        
, 0.8571428571428571                        
, 0.8                        
, 0.7142857142857143                        
, 1.0                        
, 0.8636363636363636                        
, 1.0                        
, 0.7419354838709677                        
, 0.875                        
, 0.7                        
, 0.8571428571428571                        
, 1.0                        
, 1.0                        
, 0.5714285714285714                        
, 0.5555555555555556                        
, 1.0                        
, 0.7647058823529411                        
, 0.7647058823529411                        
, 0.8                        
, 0.7142857142857143                        
, 0.8076923076923077                        
, 0.6666666666666666                        
, 0.8888888888888888                        
, 0.75                        
, 1.0                        
, 0.6923076923076923                        
, 1.0                        
, 0.0                        
, 0.6666666666666666                        
, 0.8                        
, 0.7142857142857143                        
, 0.3076923076923077                        
, 0.5416666666666666                        
, 0.6666666666666666                        
, 1.0                        
, 0.7777777777777778                        
, 1.0                        
, 0.6666666666666666                        
, 0.7                        
, 0.7272727272727273                        
, 0.0                        
, 0.625                        
, 0.75                        
, 0                        
, 0.7727272727272727                        
, 0.8181818181818182                        
, 0.6666666666666666                        
, 0.8888888888888888                        
, 0                        
, 0.8571428571428571                        
, 0.7391304347826086                        
, 0.75                        
, 0.6666666666666666                        
, 0.9                        
, 0.75                        
, 1.0                        
, 1.0                        
, 0.5                        
, 0.875                        
, 0.5                        
, 0.8461538461538461                        
, 0.6666666666666666                        
, 0.875                        
, 0.75                        
, 0.6                        
, 0.6666666666666666                        
, 0.5                        
, 0.625                        
, 0.6666666666666666                        
, 0.8                        
, 0.8780487804878049                        
, 0.6363636363636364                        
, 1.0                        
, 0.8571428571428571                        
, 0.875                        
, 0.8                        
, 0.6666666666666666                        
, 1.0                        
, 1.0                        
, 0.75                        
, 0.47368421052631576                        
, 0.2727272727272727                        
, 1.0                        
, 0.9090909090909091                        
, 1.0                        
, 0.6363636363636364                        
, 0.6                        
, 1.0                        
, 0.8636363636363636                        
, 0.8846153846153846                        
, 0.6666666666666666                        
, 1.0                        
, 0.4                        
, 0.6666666666666666                        
, 0.8125                        
, 0.8                        
, 0.75                        
, 0.6111111111111112                        
, 0.7857142857142857                        
, 0.9230769230769231                        
, 0.6666666666666666                        
, 0.6470588235294118                        
, 0.7142857142857143                        
, 0.875                        
, 0.7142857142857143                        
, 0.6666666666666666                        
, 0.8333333333333334                        
, 0.6666666666666666                        
, 0.7142857142857143                        
, 0.8333333333333334                        
, 0.0                        
, 0.7692307692307693                        
, 0.95                        
, 0.7777777777777778                        
, 0.8181818181818182                        
, 0.5882352941176471                        
, 0.8                        
, 0.8695652173913043                        
, 0.7777777777777778                        
, 0.8                        
, 1.0                        
, 0.6666666666666666                        
, 0.4166666666666667                        
, 0.8                        
, 0.6875                        
, 0.6666666666666666                        
, 0.8333333333333334                        
, 0.8181818181818182                        
, 0.8333333333333334                        
, 0.7333333333333333                        
, 1.0                        
, 0.75                        
, 0.75                        
, 1.0                        
, 0.8                        
, 0.5625                        
, 0.8421052631578947                        
, 0.8181818181818182                        
, 0.9                        
, 1.0                        
, 0.7692307692307693                        
, 0.7916666666666666                        
, 0.8888888888888888                        
, 0.875                        
, 0.6666666666666666                        
, 0.6956521739130435                        
, 0.7777777777777778                        
, 0.6923076923076923                        
, 0.6333333333333333                        
, 0.7058823529411765                        
, 0.8571428571428571                        
, 1.0                        
, 0.5833333333333334                        
, 0.9166666666666666                        
, 0.7272727272727273                        
, 1.0                        
, 0.7272727272727273                        
, 0.75                        
, 0.8888888888888888                        
, 0.8                        
, 0.8461538461538461                        
, 0.8181818181818182                        
, 0.7142857142857143                        
, 0.8571428571428571                        
, 0.5                        
, 0.75                        
, 0.6666666666666666                        
, 0.2857142857142857                        
, 1.0                        
, 0.7777777777777778                        
, 0.75                        
, 0                        
, 0.8333333333333334                        
, 0.6666666666666666                        
, 0.42857142857142855                        
, 1.0                        
, 0.9230769230769231                        
, 0.5789473684210527                        
, 0.3333333333333333                        
, 0.4                        
, 0.5333333333333333                        
, 0.8888888888888888                        
, 0.875                        
, 0.7777777777777778                        
, 0.6                        
, 0.7142857142857143                        
, 0.5714285714285714                        
, 0.5                        
, 0.6666666666666666                        
, 0.0                        
, 0.6875                        
, 0.5                        
, 0.8461538461538461                        
,]
with open('rp.pkl', 'wb') as f:
    pickle.dump(rp, f)
