from seidownpy.items import LineBlogItem

import datetime
import scrapy
import os

class LineBlogSpider(scrapy.Spider):
	URL_SYNTAX = 'http://lineblog.me/%s/?p=%s'
	name = "lineblog"

	def __init__(self, name='', first='0', last='1', *args, **kwargs):
		if not first.isdigit() or not last.isdigit():
			raise ValueError("Page number must be a positive digit")

		super(LineBlogSpider, self).__init__(*args, **kwargs)
		self.start_urls = ['http://lineblog.me/%s' % name]
		self.main_name = name
		self.page_urls = self._create_urls(first, last)

	def _create_urls(self, first=0, last=1):
		if not first.isdigit() or not last.isdigit():
			raise ValueError("Page number must be a positive digit")

		first_int = int(first)
		last_int = int(last)

		if first_int < 0 or last_int < 0:
			raise ValueError("Page number must be a positive digit")

		urls = []
		step = self._get_step(first_int, last_int)
		urls.append('http://lineblog.me/%s' % self.main_name)
		for page_number in range(first_int, last_int + 1, step):
			urls.append(self.URL_SYNTAX % (self.main_name, page_number))
		return urls

	def _get_step(self, first_int, last_int):
		if first_int >= last_int:
			return -1
		else:
			return 1

	def start_requests(self):
		for url in self.page_urls:
			yield scrapy.Request(url, callback=self.parse)

	def parse(self, response):
		articles = response.css("div#main-inner article.article")
		for article in articles:
			for url in article.css("img.pict").xpath("@src").extract():
				tempURL = url[:url.rfind('/')]
				yield LineBlogItem(item_source=self.main_name, image_urls=[tempURL])

