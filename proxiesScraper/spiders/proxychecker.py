import scrapy
import datetime
from ..items import ProxyItem


class ProxycheckerSpider(scrapy.Spider):
    name = "proxychecker"
    allowed_domains = ["checkerproxy.net"]
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    start_urls = [f"http://checkerproxy.net/api/archive/{today}"]

    def parse(self, response):
        for comb in response.json():
            if comb['timeout'] <= 1000:
                item = ProxyItem()
                item['ip'] = comb['addr']
                item['source'] = self.name
                yield item
