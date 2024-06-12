inputs=(
    111
    110
    101
    100
    011
    010
    001
    000
)


for input in ${inputs[@]}; do
    echo $input | python ../ex7.py > tmp.txt
    TMP=$(cat tmp.txt )
    echo $TMP
    if [ ${TMP} = "AtCoder" ]; then
        echo "  ↑正解"
    fi
done

\rm tmp.txt
