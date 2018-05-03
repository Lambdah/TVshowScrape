# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TvscrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tv_intro = scrapy.Field()
    tv_name = scrapy.Field()
    tv_link = scrapy.Field()
    tv_img = scrapy.Field()
    tv_episode_number = scrapy.Field()
    tv_air_date = scrapy.Field()
    tv_network = scrapy.Field()
