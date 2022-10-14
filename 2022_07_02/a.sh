#! /bin/bash
for ((i=0; i<=100; i++))
do
    echo $i | python a.py
done > aout.txt
