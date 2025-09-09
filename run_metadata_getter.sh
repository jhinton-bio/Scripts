#!/bin/bash

#this script runs the python metadata json parser.

#json assembly stats and accession numbers delimited by spaces
file=$1

#run python script looping through that file

while read -r line
do
	python3 /mnt/md0/mosquito_analysis/json_reader_5.3.py $(echo ${line} $file)
	
done< ${file}
