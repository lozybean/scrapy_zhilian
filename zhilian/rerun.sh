#!/usr/bin/env bash

rm text.json
scrapy crawl zhilian -o text.json
python json_parse.py
# rm text.csv
# scrapy crawl zhilian -o text.csv
