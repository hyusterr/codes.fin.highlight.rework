mkdir demo
for company in $(cat $1); do #CIKs.txt
    echo $company
    mkdir demo_top1/$company
    for item in ITEM1 ITEM10 ITEM11 ITEM12 ITEM13 ITEM14 ITEM15 ITEM1A ITEM1B ITEM2 ITEM3 ITEM4 ITEM5 ITEM6 ITEM7 ITEM7A; do
        for t in 0 1 2; do
            grep TYPE_${t}$'\t'${company} $2 | grep -i _${item}_ | sed "s/^TYPE_${t}	//"  > demo/$company/$item.type$t
        done
    done
done
# TYPE_0  1094348_13_item7_p3_s1
