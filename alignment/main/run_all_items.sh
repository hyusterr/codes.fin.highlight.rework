mkdir data/all_item
for item in /tmp2/cwlin/fintext-new/test-collections/rand200/predict-all/prediction/by-item/*
    do 
        echo $item
        item_name=$(echo $item | rev | cut -d/ -f1 | rev)
        item_path=data/all_item/$item_name
        echo dealing $item_path ...
        mkdir $item_path
        echo running seperated by company ...
        bash data/by_company.sh $item/rand200_collections.txt $item_path
        echo running alignment for each company ...
        for f in $item_path/*
            do 
                company=$(echo $f | rev | cut -d'/' -f 1 | rev | cut -d'.' -f1)
                echo running $company $item_name ...
                python3 get-top10-bm25-lda-rouge-staged.py -f $f -o results/cross-seg/sort_by_rouge/top10/ -r record/cross-seg/sort_by_rouge/
                for j in results/cross-seg/sort_by_rouge/top10/${company}_*_${item_name}.json
                    do 
                        fname=$(echo $j | cut -d '/' -f 5)
                        python3 max-diff-drop-staged.py -f $j -o results/cross-seg/sort_by_rouge/maxdiff/$fname &
                    done
                wait
                for l in results/cross-seg/sort_by_rouge/maxdiff/${company}_*_${item_name}.json
                    do
                        jname=$(echo $l | cut -d'/' -f5)
                        python3 get-SBERT-cossim-lda.py -c $f -j $l -o results/cross-seg/sort_by_rouge/sbert/$jname
                    done
            done
    done        
