from seidownpy.items import KeyakiItem

import scrapy

class KeyakiSpider(scrapy.Spider):
    URL_SYNTAX = 'http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&page=%s&cd=member&ct=%s'
    name = 'keyaki'

    def __init__(self, name='', first="0", last="1", *args, **kwargs):
		super(KeyakiSpider, self).__init__(*args, **kwargs)
		self.start_urls = ['http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&ct=%s' % name]
		self.main_name = name
		self.first_int = self._get_int(first)
		self.last_int = self._get_int(last)

    def _get_int(self, int_str):
		if not int_str.isdigit() or int(int_str) < 0:
			raise ValueError("Page number must be a positive digit")
		return int(int_str)

    def start_requests(self):
        first_int = self.first_int
        last_int = self.last_int
        step = self._get_step(first_int, last_int)
        for page_number in range(first_int, last_int + 1, step):
            yield scrapy.Request(self.URL_SYNTAX % (page_number, self.main_name), callback=self.parse)

    def _get_step(self, first_int, last_int):
		if first_int >= last_int:
			return -1
		else:
			return 1

    def parse(self, response):
        box_main = response.css("div.keyaki-blog_list div.l-wrapper div.l-content div.l-inner div.box-content div.box-main")
        main_contents = box_main.css('img')
        for content in main_contents:
            url = content.xpath("@src").extract_first()
            yield KeyakiItem(image_urls=[url])