#!/usr/bin/env bash

if [ ! -z "$1" ]; then
    files=("$(ls -1A $1)")
    for f in ${files[@]}; do
        [ -L $f ] && unlink $f
        ln -s "$1/$f" && echo "Linked $f from $1"
    done
    ls -lA
else
    echo "Argument is required"
fi

# if [ ! -L "../venv/lib/python3*/site-packages/centralCLI" ]; then
#     ln -s ../venv/lib/python3*/site-packages/centralCLI ../lib/centralCLI
# fi

