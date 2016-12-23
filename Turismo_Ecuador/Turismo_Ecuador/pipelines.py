# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json as js
class TurismoEcuadorPipeline(object):
    arreglo = []
    def process_item(self, item, spider):
        with open("DatosTuristicoZamoraChinchipe.json",mode='a+') as f:
            f.write(js.dumps(dict(item), indent=4, ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8'))
