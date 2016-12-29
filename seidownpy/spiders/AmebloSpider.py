from seidownpy.items import AmebloItem

import datetime
import scrapy
import logging

URL_SYNTAX = 'http://ameblo.jp/%s/page-%s.html'

class AmebloSpider(scrapy.Spider):
	name = "ameblo"
	start_urls = ["http://ameblo.jp/"]

	def __init__(self, name='', first=0, last=1, *args, **kwargs):
		if not first.isdigit() or not last.isdigit():
			raise ValueError("Page number must be a positive digit")
		if first >= last:
			raise ValueError("First page must always be smaller")

		super(AmebloSpider, self).__init__(*args, **kwargs)
		self.start_urls = ['http//ameblo.jp/%s/' % name]
		self.main_name = name
		self.first = int(first)
		self.last = int(last)

		if self.first < 0 or self.last < 0:
			raise ValueError("Page number must be a positive digit")

	def start_requests(self):
		for page_number in range(self.first, self.last + 1):
			url = URL_SYNTAX % (self.main_name, page_number)
			yield scrapy.Request(url, callback=self.parse)

	def parse(self, response):
		url = response.css("div#main").xpath("//article[@data-unique-ameba-id='%s']" % self.main_name)
		for u in url.xpath("//a/img"):
			imageURL = u.xpath("@src").extract_first()
			yield AmebloItem(item_id='', file_urls=[imageURL])

	def parse_image(self, response):
		print ""
		# imageURL = img.extract_first()
		# print imageURL
		# yield AmebloItem(item_id='', file_urls=[imageURL])
		yield None
