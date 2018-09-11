import scrapy
import os
import enchant
#import os

class NikeSpider(scrapy.Spider):
	name = 'Nike'
	
	def start_requests(self):
		self.start_urls = ['http://www.twitter.com/nikestore']
		self.allowed_domains = ['www.nike.com','www.twitter.com']
		yield scrapy.Request(url = 'http://www.twitter.com/nikestore', callback=self.parse)
	
	def parse(self, response):
		dictionary = enchant.Dict('en_US')
		tweet = response.css('p.TweetTextSize').extract_first().split()
		print(tweet)
		words = []
		temp = str()
		for word in tweet:
			if word.startswith('\'') or word.endswith('\''):
				word = word.replace('\'','')

			if word.startswith('KD') or word.startswith('AJ'):
				words.append(word)			

			elif word != ' ' and dictionary.check(word):	
				words.append(word)
			elif word.endswith('</p>'):
				words.append(word[0:-4])
				
			elif word[0:25] == 'data-aria-label-part="0">':
				words.append(word[25:])
			elif word[0:17] == 'data-expanded-url':
				for char in word[19:]:
					if char == '"':
						break
					else:			
						temp = temp + char
		
				words.append(temp)
				temp = ""
			else:
				try: word1, word2 = word.split('/')
				except: continue
				if word1 != '':
					if dictionary.check(word1):
						words.append(word1)
				if word2 != '':
					if dictionary.check(word2):
						words.append(word2)
		print("words: ",words)
		#link = response.css('span.js-display-url::text').extract_first() 	#exctract first tweet
		
		#tweet = 'http://'+tweet
		
		files = os.listdir('../.gitignore/')
	#	print(files)
	#	print(os.getcwd())
		if 'NikeTwitterStrings.txt' in files:
			os.remove('../.gitignore/NikeTwitterStrings.txt')
		newfile = open('../.gitignore/NikeTwitterStrings.txt','w')
		for word in words:
			newfile.write(word + ' ')
		newfile.close()
		os.chdir('..')
		
		#webbrowser.open(tweet)
		#print(tweet)
		#response = scrapy.Request(url = tweet, callback = self.buyShoes)
		#print(response)
	

