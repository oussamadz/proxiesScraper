import scrapy
from ..items import ProxyItem


class ProxyDailySpider(scrapy.Spider):
    name = "proxy-daily"
    allowed_domains = ["proxy-daily.com"]
    start_urls = ["http://proxy-daily.com/"]

    def parse(self, response):
        proxies = response.xpath("//div[contains(@class, 'freeProxyStyle')]/text()").get().split("\n")
        for prox in proxies:
            if prox == "":
                continue
            item = ProxyItem()
            item['ip'] = prox
            item['source'] = self.name
            yield item
