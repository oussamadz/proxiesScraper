import scrapy
from ..items import ProxyItem


class HidemynameSpider(scrapy.Spider):
    name = 'hidemyname'
    allowed_domains = ['hidemy.name']
    start_urls = ['https://hidemy.name/en/proxy-list/']

    def parse(self, response):
        ips = response.xpath("//div[@class='table_block']/table/tbody/tr/td[1]/text()").getall()
        ports = response.xpath("//div[@class='table_block']/table/tbody/tr/td[2]/text()").getall()
        for ip, port in zip(ips, ports):
            item = ProxyItem()
            item['ip'] = f"{ip}:{port}"
            item['source'] = self.name
            yield item
