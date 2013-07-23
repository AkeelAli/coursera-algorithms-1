#!/bin/bash

ABSOLUTE_MIN_CUT=10000

for i in {1..100}
do
    python optimized_min_cut.py
    MIN=$?
    
    if [ $MIN -lt $ABSOLUTE_MIN_CUT ] 
    then
        ABSOLUTE_MIN_CUT=$MIN
    fi
done

echo "ABSOLUTE_MIN_CUT = $ABSOLUTE_MIN_CUT"
