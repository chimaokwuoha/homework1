from steam.items import steamItem
from scrapy import Spider, Request

class steam_spider(Spider):
	name = 'steam_spider'
	allowed_urls = ['http://store.steampowered.com/']
	start_urls = ['http://store.steampowered.com/tags/en/Action/#p='+str(i)+'&tab=NewReleases' ]
	#the start url has to be manual changed becuases stema limits mass scrapping 
	
	def parse(self, response):

		new_releases = response.xpath('//*[@id="NewReleasesRows"]//div[@class="tab_item_name"]//text()').extract()
		#get a list of titles

		money = response.xpath('//*[@id="NewReleasesRows"]//div[@class="discount_final_price"]//text()').extract()
		#get a list of prices

		tags = response.xpath('//*[@id="NewReleasesRows"]//span//text()').extract()
		#gete= the tags for each games

		for i in range(len(new_releases)):

			#stor info in tags
			item = steamItem()
			item['title'] = new_releases[i]	
			item['tags']=tags		
			
			#note to self:remember some games are free. If they are free just insert 0 dollars as price value 
			try:
				item['price'] = money[i]
			except:
				item['price']='0'


			yield item


