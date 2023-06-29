for l in results/cross-seg/sort_by_rouge/missing_maxdiff/*.json
    do
        jname=$(echo $l | cut -d'/' -f5)
        echo $jname
        python3 get-SBERT-cossim-lda.py -c data/cross-seg.all.collections -j $l -o results/cross-seg/sort_by_rouge/missing_sbert/$jname
    done
