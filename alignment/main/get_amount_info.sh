# python3 get-all-type-pairs.py -c data/cross-seg.all.collections -d results/cross-seg/sort_by_rouge/sbert_top1/ -rs 0.0870 -sn 0.9978 > all.type.alignment.result
python3 get-all-type-pairs.py -c data/cross-seg.all.collections -d results/cross-seg/sort_by_rouge/sbert_item7/ -rs 0.6296 -sn 0.9011 > all.type.alignment.result.item7
echo all pairs:
wc -l all.type.alignment.result.item7
echo unique this year segments:
cut -d$'\t' -f 3 all.type.alignment.result.item7 | sort -u | wc -l
for t in TYPE_0 TYPE_1 TYPE_2
    do
        echo $t number of pairs:
        grep $t all.type.alignment.result.item7 | wc -l
        echo $t number of unique this year segments:
        grep $t all.type.alignment.result.item7 | cut -d$'\t' -f 3 | sort -u > $t.uniqID
        wc -l $t.uniqID
    done
