# python3 get-top10-bm25-lda-rouge-staged.py -f data/sentence/100378.txt -o results/sentence/sort_by_rouge/top10/ -r record/sentence/sort_by_rouge/
# python3 max-diff-drop-staged.py -f results/sentence/sort_by_rouge/top10/100378_14_ITEM7.json -o results/sentence/sort_by_rouge/maxdiff/100378_14_ITEM7.json

company=$(echo $1 | rev | cut -d'/' -f 1 | rev | cut -d'.' -f 1)
echo $company
python3 get-top10-bm25-lda-rouge-staged.py -f $1 -o results/cross-seg/sort_by_rouge/top10/ -r record/cross-seg/sort_by_rouge/

for f in results/cross-seg/sort_by_rouge/top10/$company*
    do
        fname=$(echo $f | cut -d'/' -f5) && python3 max-diff-drop-staged.py -f $f -o results/cross-seg/sort_by_rouge/maxdiff/$fname &
    done
wait

for j in results/cross-seg/sort_by_rouge/maxdiff/$company*
    do
        jname=$(echo $j | cut -d'/' -f5)
        python3 get-SBERT-cossim-lda.py -c $1 -j $j -o results/cross-seg/sort_by_rouge/sbert/$jname
    done
