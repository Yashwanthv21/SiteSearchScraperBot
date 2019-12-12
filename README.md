# SiteSearchScraperBot
Scrapes the given sites and saves the data. Returns the corresponding URL when a keyword in the page is searched

## Requirements
1. Elastic Search
2. Python 3.7
3. python libs used are scrapy, elasticsearch
4. Dejavu Elastic browser extension

## Installations
1. Install [elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html#install-elasticsearch)
2. Install (Anaconda) python 3.7 and pip 
3. open terminal install python libs `pip install scrapy elasticsearch`
4. Install chrome extension [dejavu elastic chrome extension](https://chrome.google.com/webstore/detail/dejavu-elasticsearch-web/jopjeaiilkcibeohjdmejhoifenbnmlh)
5. In Dejavu enter the local elatic url and the index name as `http://localhost:9200` and index as `testsites` 

## Steps to run the Crawler
1. Open `a_spider.py` inside the spiders folder. This is the main code for the spider
2. The data crawled here is sent to `pipelines.py` where it is added to Elastic search.
3. To run the script, change the URL in `a_spider.py` to the site you want to crawl 
4. open terminal/command prompt into the first directory `harriscounty` 
6. Make sure you start your elastic node using `bin\elastic` from the elastic directory and your node is running [http://localhost:9200](http://localhost:9200)
5. Now run `scrapy crawl asites` and wait for the data to be crawled and ingested
