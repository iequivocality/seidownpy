# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AmebloItem(scrapy.Item):
	item_id = scrapy.Field()
	file_urls = scrapy.Field()
	files = scrapy.Field()

class SingleItem(scrapy.Item):
	file_urls = scrapy.Field()
	files = scrapy.Field()

class LineBlogItem(scrapy.Item):
	file_urls = scrapy.Field()
	files = scrapy.Field()