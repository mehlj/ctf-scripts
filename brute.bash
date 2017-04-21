#!/usr/bin/env bash

for i in {1..4096}
do
    FLAG="$(/problems/bd058e83a119c78a006543d23d9f6422/bashloop $i)"
    if [ "$FLAG" != "Nope. Pick another number between 0 and 4096" ]
    then
        echo $FLAG
        exit
    fi
done

