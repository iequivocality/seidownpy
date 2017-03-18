from seidownpy.items import AmebloItem

import datetime
import scrapy
import os

class AmebloSpider(scrapy.Spider):
	ENTRY_URL_SYNTAX = 'http://ameblo.jp/%s/entry-%s.html' 
	PAGE_URL_SYNTAX = 'http://ameblo.jp/%s/page-%s.html'
	name = "ameblo"
	start_urls = ["http://ameblo.jp/"]

	def __init__(self, name='', entry=None, first="0", last="1", *args, **kwargs):
		super(AmebloSpider, self).__init__(*args, **kwargs)
		self.start_urls = ['http://ameblo.jp/%s/' % name]
		self.main_name = name
		self.entry_no = entry
		self.first_int = self._get_int(first)
		self.last_int = self._get_int(last)

	def _get_int(self, int_str):
		if not int_str.isdigit() or int(int_str) < 0:
			raise ValueError("Page number must be a positive digit")
		return int(int_str)

	def start_requests(self):
		if self.entry_no is None:
			first_int = self.first_int
			last_int = self.last_int
			step = self._get_step(first_int, last_int)
			for page_number in range(first_int, last_int + 1, step):
				yield scrapy.Request(self.PAGE_URL_SYNTAX % (self.main_name, page_number), callback=self.parse)
		else:
			yield scrapy.Request(self.ENTRY_URL_SYNTAX % (self.main_name, self.entry_no), callback=self.parse)

	def _get_step(self, first_int, last_int):
		if first_int >= last_int:
			return -1
		else:
			return 1

	def parse(self, response):
		main = response.css("div#main")
		tile = main.xpath("//div[@amb-component='tiles']")
		if (len(tile.extract()) > 0):
			tileList = tile.xpath("//ul[@amb-component='tileList']")
			itemBody = tileList.xpath("//div[@amb-component='tileItem']").xpath("//div[@amb-component='tileItemBody']")
			itemTitleLink = itemBody.xpath("//h2[@amb-component='tileItemTitle']").xpath("//a[@class='skin-titleLink']")
			for link in itemTitleLink:
				yield scrapy.Request(link.xpath("@href").extract_first(), callback=self.parse)
			return

		default = main.xpath("//article[@data-unique-ameba-id='%s'] | //div[@data-unique-ameba-id='%s']" % (self.main_name, self.main_name))
		if (len(default.extract()) > 0):
			for u in default.xpath("//a/img"):
				imageURL = u.xpath("@src").extract_first()
				imageID = os.path.basename(imageURL).split("?")[0]
				yield AmebloItem(item_id=imageID, image_urls=[imageURL])
