from seidownpy.items import TumblrItem

import scrapy

class TumblrSpider(scrapy.Spider):
	FIRSTPAGE_URL_SYNTAX = 'http://%s.tumblr.com'
	OTHERPAGE_URL_SYNTAX = 'http://%s.tumblr.com/page/%s'
	name = "tumblr"

	def __init__(self, name='', first='1', last='1', *args, **kwargs):
		if not first.isdigit() or not last.isdigit():
			raise ValueError("Page number must be a positive digit")

		super(TumblrSpider, self).__init__(*args, **kwargs)
		self.main_name = name
		self.start_urls = [self.FIRSTPAGE_URL_SYNTAX % name]
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
			urls.append(self.OTHERPAGE_URL_SYNTAX % (self.main_name, page_number))
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
		for photo_type_item in self._parse_photo_type(response):
			yield photo_type_item

		for photoset_type_item in self._parse_photoset_type(response):
			yield photoset_type_item

	def _parse_photo_type(self, response):
		post_contents = response.css("div.post-type-photo div.post-content")
		for post_content in post_contents:
			highres = post_content.css("a.high-res").xpath("@href").extract_first()
			yield TumblrItem(item_id='', item_source=self.main_name, image_urls=[highres])

	def _parse_photoset_type(self, response):
		post_contents = response.css("div.post-type-photoset div.post-content")
		for post_content in post_contents:
			iframe = post_content.css("iframe.photoset")
			url = iframe.xpath("@src").extract_first()
			yield scrapy.Request(url, callback=self.parse_photo_from_photoset)

	def parse_photo_from_photoset(self, response):
		photoset_rows = response.css("div.photoset div.photoset_row")
		for photoset_row in photoset_rows:
			photoset_photos = photoset_row.css("a.photoset_photo")
			yield self._extract_items_from_photoset_photos(photoset_photos)

	def _extract_items_from_photoset_photos(photoset_photos):
		for photoset_photo in photoset_photos:
			photoset_photo_url = photoset_photo.xpath("@href").extract_first()
			yield TumblrItem(item_id='', item_source=self.main_name, image_urls=[photoset_photo_url])