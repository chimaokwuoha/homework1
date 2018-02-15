# -*- coding: utf-8 -*-
from scrapy import Item, Field
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

class gamereviewsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    review = Field()
    rating=Field()
    # name = scrapy.Field()
    pass
