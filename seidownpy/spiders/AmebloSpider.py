from seidownpy.items import AmebloItem

import datetime
import scrapy
import os

class AmebloSpider(scrapy.Spider):
	URL_SYNTAX = 'http://ameblo.jp/%s/page-%s.html'
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
		url = response.css("div#main").xpath("//article[@data-unique-ameba-id='%s']" % self.main_name)
		for u in url.xpath("//a/img"):
			imageURL = u.xpath("@src").extract_first()
			imageID = os.path.basename(imageURL).split("?")[0]
			yield AmebloItem(item_id=imageID, file_urls=[imageURL])
