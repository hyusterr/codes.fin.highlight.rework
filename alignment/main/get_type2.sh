python3 get-type2-pairs-lda.py -d results/cross-seg/sort_by_rouge/sbert/ -c data/cross-seg-collection.txt -rs 0.6296 -sn 0.9011 -ln 0 -pt1 false > type2.segments
# python3 get-type2-pairs-lda.py -d results/sentence/sort_by_rouge/sbert/ -c data/sentence-collection.txt -rs 0.6296 -sn 0.9008 -ln 0 -pt1 false > type2.sentence
# python3 filter_type2.py -c data/sentence-collection.txt -t type2.sentence > type2.sentence.filter
python3 filter_type2.py -c data/cross-seg-collection.txt -t type2.segments > type2.segments.filter


echo 'type2.sentence:'; wc -l type2.sentence.filter;
# echo 'sentence type1 error:'
# grep TYPE1_ERROR type2.sentence.filter | wc -l
# echo 'sentence diff context:'
# grep DIFF_CONTEXT type2.sentence.filter | wc -l
echo 'type2.segments:'; wc -l type2.segments.filter;
# echo 'segment type1 error:'
# grep TYPE1_ERROR type2.segments.filter | wc -l
# echo 'segment diff context:'
# grep DIFF_CONTEXT type2.segments.filter | wc -l
