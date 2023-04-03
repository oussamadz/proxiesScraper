#!/bin/bash

cd ~/proxiesScraper/ || return
source ~/env/bin/activate
rm -f data.csv

for var in $(scrapy list)
do
	scrapy crawl $var; 
done

python checker.py

