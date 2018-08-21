import scrapy
import os

class TwitterSpider(scrapy.Spider):
	name = 'Twitter'	
	
	def start_requests(self):
		self.start_urls = ['http://www.twitter.com/nikestore']
		self.allowed_domains = ['www.nike.com','www.twitter.com']
		yield scrapy.Request(url = 'http://www.twitter.com/nikestore/status/1028276098768007169', callback=self.parse)

	def parse(self, response):
		os.chdir('../.gitignore')
		if 'NikeStore.html' in os.listdir():
			os.remove('NikeStore.html')
		newfile = open('NikeStore.html','wb')
		newfile.write(response.body)
		newfile.close()	
