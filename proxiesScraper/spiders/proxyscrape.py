import scrapy
from ..items import ProxyItem

class ProxyscrapeSpider(scrapy.Spider):
    name = 'proxyscrape'
    allowed_domains = ['api.proxyscrape.com']
    start_urls = ["https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all"]

    def parse(self, response):
        proxies = response.text.replace("\r", "").split("\n")
        for prox in proxies:
            item = ProxyItem()
            item['ip'] = prox
            item['source'] = self.name
            yield item
