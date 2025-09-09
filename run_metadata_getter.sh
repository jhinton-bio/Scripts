#!/bin/bash

#this script runs the python metadata json parser.

#jsonl assembly reports and accession numbers delimited by spaces
file=$1

#run python script looping through that file

while read -r line
do
	python3 json_reader_5.3.py $(echo ${line} $file)
	
done< ${file}
