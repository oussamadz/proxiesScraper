
# proxiesScraper

Proxies scraper is a scrapy script used to crawl publicly available proxies from different sources to later store them and rank according to uptime and latency. 

## how it works
The project consists of two processes :
### 1.  Scrapy Spiders 
For each source where you can add new source by creating new spider for it. Scrapy will save the scraped proxies into a new `data.csv` file every time it runs. 
### 2.  Python Checker Script
that will use multi-threading to check each proxy from the csv file if it is up and responds in less than 1s, some parameters such as response time and on which website to test the proxy can be easilly changed later in the script. 

At the end, the checker script in `good_proxies` folder will save a txt file named with the same date containing all successfully connected proxies.
## usage 
Preferably, using systemd timers to launch `startall.sh` script that will run all spiders and check proxies when done, because systemctl will later save a log of what the script outputs. this way you get new fresh and ready proxies everyday 
## Authors

- [@oussamadz](https://www.github.com/oussamadz)

