from seidownpy.items import SingleItem

import scrapy

class SingleSpider(scrapy.Spider):
	name = "single"

	def __init__(self, link='', *args, **kwargs):
		super(SingleSpider, self).__init__(*args, **kwargs)
		self.start_urls = [link]

	def parse(self, response):
		imgs = response.xpath("//img")
		for img in imgs:
			imageURL = img.xpath("@src").extract_first()
			yield SingleItem(file_urls=[imageURL])

