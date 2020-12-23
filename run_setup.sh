#!/usr/bin/env bash
source ~/anaconda3/etc/profile.d/conda.sh

#will exit if the file is not present
packages=$(cat "requirements.txt") || exit

echo "the following core packages will be installed into the new conda env. stocks"
echo $packages

#we actually need word splitting here, so no quotes
conda create -n stocks $packages

if conda env list | grep "stocks" >/dev/null
then
    echo "environment has been created!"
    echo "setting it up as active"
    conda activate stocks
    echo "you are all set!"
    exit 0
else
    echo "error with activating/creating the environment!" > /dev/stderr
    exit 1
fi
