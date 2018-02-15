from gamereviews.items import gamereviewsItem
from scrapy import Spider, Request

class steam_spider(Spider):
	name = 'gamereviews_spider'
	allowed_urls = ['https://www.gamespot.com/reviews/']
	start_urls = ['https://www.gamespot.com/reviews/?sort=date&page='+str(i) for i in range(2,670)]
	#flip through the url 
	

	def parse(self, response):

		gamereviews = response.xpath('//*[@id="js-sort-filter-results"]//section//article//p').extract()
		rating= response.xpath('//*[@id="js-sort-filter-results"]//section//article//a/div//div//div//span//text()').extract()
		#extract the rating and game reviews

		for i in range(len(gamereviews)):
			#store info in csv file
			item = gamereviewsItem()
			item['review'] = gamereviews[i]	
			item['rating']=rating[i]

			yield item



