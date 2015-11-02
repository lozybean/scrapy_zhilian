#!/usr/bin/env bash

rm text.json
scrapy crawl zhilian -o text.json
# rm text.csv
# scrapy crawl zhilian -o text.csv
