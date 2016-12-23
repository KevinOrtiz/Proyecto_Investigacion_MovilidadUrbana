# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import unidecode
import string
from scrapy.loader.processors import TakeFirst, MapCompose,Join


class TurismoEcuadorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nombreLugar = scrapy.Field(
                                input_processor = MapCompose(unicode.strip,
                                    lambda x:unidecode.unidecode(x),
                                    lambda y:string.replace(y,'\n','')),
                                out_processor = Join(),
                            )
    latitud = scrapy.Field()
    longitud = scrapy.Field()
    tituloComentarios = scrapy.Field(
                                input_processor = MapCompose(unicode.strip,
                                     lambda x:unidecode.unidecode(x),
                                     lambda y:string.replace(y,'\n','')),
                                out_processor = Join(),
                            )
    comentarios = scrapy.Field(

                                input_processor = MapCompose(unicode.strip,
                                     lambda x:unidecode.unidecode(x),
                                     lambda y:string.replace(y,'\n','')),
                                out_processor = Join(),

                            )
