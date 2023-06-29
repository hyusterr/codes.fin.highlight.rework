company=$(echo $1 | rev | cut -d'/' -f 1 | rev | cut -d'.' -f 1)
echo $company
python3 get-top10-bm25-lda-rouge-staged.py -f $1 -o sentence/top10-staged-results/

for f in sentence/top10-staged-results/$company*
    do
        fname=$(echo $f | cut -d'/' -f3) && python3 max-diff-drop-staged.py -f $f -o sentence/max-diff-drop-results-staged/$fname &
    done
wait

for j in sentence/max-diff-drop-results-staged/$company*
    do
        jname=$(echo $j | cut -d'/' -f3)
        python3 get-SBERT-cossim-lda.py -c $1 -j $j -o sentence/sbert-and-lda-results-staged/$jname
    done
