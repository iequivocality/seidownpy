# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import FilesPipeline

class AmebloImagePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
        	new_file_url = file_url.split("?")[0]
        	yield scrapy.Request(new_file_url)
