import scrapy

from spider_one.items import DevShedItem

class DevShedSpider(scrapy.Spider):
    name = "devshed"
    allowed_domains = ["forums.devshed.com"]
    start_urls = ["https://forums.devshed.com/python-programming-11/1.html"]

    def parse(self, response):
        for sel in response.xpath('//*[@id="threads"]/li/div/div[1]/div/h3'):
            item = DevShedItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item
