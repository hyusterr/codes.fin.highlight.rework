for t in 0 1 2; do
    grep TYPE_${t} $1  | sed "s/^TYPE_${t}	//"  > demo.missing.pairs.type$t
done
