import scrapy
from ..items import ProxyItem

class FreeproxySpider(scrapy.Spider):
    name = 'freeproxy'
    allowed_domains = ['www.freeproxy.world']
    start_urls = ['https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=%d' %x for x in range(1, 510)]
    custom_settings =  { 
                "DOWNLOAD_DELAY": "1"
            }

    def parse(self, response):
        ips = response.xpath("//table[@class='layui-table']/tbody/tr/td[1]/text()").getall()
        ports = response.xpath("//table[@class='layui-table']/tbody/tr/td[2]/a/text()").getall()
        for ip, port in zip(ips, ports):
            item = ProxyItem()
            ip = ip.replace("\n", "")
            item['ip'] = f"{ip}:{port}"
            item['source'] = self.name
            yield item
