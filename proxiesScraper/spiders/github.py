import scrapy
from ..items import ProxyItem


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['raw.githubusercontent.com']
    start_urls = ['https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt']

    def parse(self, response):
        proxies = response.text.split("\n")
        for prox in proxies:
            item = ProxyItem()
            item['ip'] = prox
            item['source'] = "github"
            yield item
