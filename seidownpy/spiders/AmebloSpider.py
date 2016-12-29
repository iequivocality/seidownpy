from seidownpy.item import AmebloItem
import datetime
import scrapy

class AmebloSpider(scrapy.Spider):
	name = "ameblo"
	start_urls = ["http://ameblo.jp/"]