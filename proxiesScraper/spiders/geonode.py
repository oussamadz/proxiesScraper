import scrapy
from ..items import ProxyItem

class GeonodeSpider(scrapy.Spider):
    name = 'geonode'
    allowed_domains = ['proxylist.geonode.com']
    start_urls = ['https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc']

    def parse(self, response):
        for prox in response.json()['data']:
            item = ProxyItem()
            item['ip'] = f"{prox['ip']}:{prox['port']}"
            item['source'] = "geonode"
            yield item
