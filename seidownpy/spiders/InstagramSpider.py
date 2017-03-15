from seidownpy.items import InstagramItem
import scrapy

class InstagramSpider(scrapy.Spider):
	URL_SYNTAX = 'https://www.instagram.com%s'
	name = "instagram"

	def __init__(self, name='', *args, **kwargs):
		self.main_name = '/%s' % (name)
		super(InstagramSpider, self).__init__(*args, **kwargs)

	def start_requests(self):
		yield scrapy.Request(self.URL_SYNTAX % (self.main_name), callback=self.parse)

	def parse(self, response):
		main = response.css("#react-root").css("main._6ltyr")
		article = main.css("article._42elc")
		for _myci9 in article.css("._nljxa").css("._myci9"):
			col = _myci9.css("._8mlbc").xpath("@href").extract()
			for item in col:
				yield scrapy.Request(url=self.URL_SYNTAX % (item), callback=self.parse_item)

		next_page = article.css("._8imhp").xpath("@href")
		if len(next_page) > 0:
			yield scrapy.Request(url=self.URL_SYNTAX % (next_page.extract_first()), callback=self.parse)

	def parse_item(self, response):
		main = response.css("#react-root").css("main._6ltyr")
		article = main.css("article._ksjel > div")
		for _jjzlb in article.css("._22yr2").css("._jjzlb"):
			col = _jjzlb.css("img").xpath("@src").extract_first()
			yield InstagramItem(item_source=self.main_name, image_urls=[col])