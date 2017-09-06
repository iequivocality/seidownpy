# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AmebloItem(scrapy.Item):
	item_id = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()

class KeyakiItem(scrapy.Item):
	item_id = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()

class SingleItem(scrapy.Item):
	image_urls = scrapy.Field()
	images = scrapy.Field()

class LineBlogItem(scrapy.Item):
	item_source = scrapy.Field();
	image_urls = scrapy.Field()
	images = scrapy.Field()

class TumblrItem(scrapy.Item):
	item_id = scrapy.Field()
	item_source = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()

class InstagramItem(scrapy.Item):
	item_source = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field() 