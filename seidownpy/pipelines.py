# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class SeidownImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['image_urls']:
        	if file_url is None:
        		continue
        	new_file_url = file_url
        	if "?" in file_url:
        		new_file_url = file_url.split("?")[0]
        	yield scrapy.Request(new_file_url)
