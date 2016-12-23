import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import selector
from scrapy import loader
from scrapy.loader import ItemLoader
from Turismo_Ecuador.items import TurismoEcuadorItem

class extraccionDatosEcuador(CrawlSpider):
    name = "Turismo_Ecuador"

    allowed_domains = ['tripadvisor.co']

    start_urls = ['https://www.tripadvisor.co/Attractions-g2651602-Activities-Zamora_Chinchipe_Province.html']

    rules = [
      Rule(LinkExtractor(restrict_xpaths="//div[@class='pagination']/div[@class='unified pagination ']/a"),follow=True),
      Rule(LinkExtractor(restrict_xpaths="//div[@id='FILTERED_LIST']/div/div[@class='element_wrap']/div[@class='wrap al_border attraction_element']/div[@class='photo_booking non_generic']/a"), callback='parseInformation',follow=True),
    ]

    def parseInformation(self,response):
        l = ItemLoader(item = TurismoEcuadorItem(),response = response)
        l.add_xpath('nombreLugar',"//div[@id='HEADING_GROUP']/div[@class='headingWrapper easyClear ']/div[@class='heading_name_wrapper']/h1/text()")
        l.add_xpath('latitud',"//div[@id='NEARBY_TAB']/div[@class='content']/div[@class='mapWrap']/div[@class='mapContainer']/@data-lat")
        l.add_xpath('longitud',"//div[@id='NEARBY_TAB']/div[@class='content']/div[@class='mapWrap']/div[@class='mapContainer']/@data-lng")
        l.add_xpath('tituloComentarios',"//div[@class='wrap']/div[@class='quote']/a/span/text()")
        l.add_xpath('comentarios',"//div[@class='wrap']/div[@class='entry']/p[@class='partial_entry']/text()")
        yield l.load_item()
