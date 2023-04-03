import scrapy
from ..items import ProxyItem

class FplSpider(scrapy.Spider):
    name = 'fpl'
    allowed_domains = ['free-proxy-list.net']
    start_urls = ['https://free-proxy-list.net/']

    def parse(self, response):
        ips = response.xpath("//div[contains(@class, 'fpl-list')]/table/tbody/tr/td[1]/text()").getall()
        ports = response.xpath("//div[contains(@class, 'fpl-list')]/table/tbody/tr/td[2]/text()").getall()
        for ip, port in zip(ips, ports):
            item = ProxyItem()
            item['ip'] = f"{ip}:{port}"
            item['source'] = "fpl"
            yield item
