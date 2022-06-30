from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request


class viradaCultural(CrawlSpider):
    name = "virada_cultural"
    start_urls = ["https://catracalivre.com.br/agenda/programacao-completa-virada-cultural-sp-2022/"]

    def parse(self, response):
        body_sel = Selector(response)
        textos = body_sel.xpath("//p//span").extract()

