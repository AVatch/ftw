import json

from scrapy.spider 		import BaseSpider
from scrapy.http 		import Request
from ftw_scrapers.items import Game, Achievement


class XboxOneGameListSpider(BaseSpider):
	name = 'xboxOneGameList'
	allowed_domains = ["xboxachievements.com"]
	# start_urls = ["http://www.xboxachievements.com/games/xbox-one/" + str(page) + "/" for page in range(1,10)]
	start_urls = ["http://www.xboxachievements.com/games/xbox-one/" + str(page) + "/" for page in range(1,2)]

	def parse(self, response):
		for row in response.xpath('//div[@class="divtext"]/table/tr'):
			cols = row.xpath('td')
			if len(cols) == 5:
				game = Game()
				game['title'] = cols[1].xpath('a/strong/text()').extract_first()
				game['artwork'] = cols[0].xpath('a/img/@src').extract_first()
				game['achievement_count'] = cols[2].xpath('text()').extract_first()
				game['achievement_list_url'] = cols[0].xpath('a/@href').extract_first()
				
				if game['title'] and game['artwork'] and game['achievement_count'] and game['achievement_list_url']:
					url = 'http://xboxachievements.com' + game['achievement_list_url']
					yield Request(url, callback=self.parse_achievements)
					yield game


	def parse_achievements(self, response):

		game = response.xpath('//h1[@class="tt"]/text()').extract_first()
		game = game.replace('Achievements', '').rstrip()

		rows = response.xpath('//div[@class="divtext"]/table/tr')[3:]
		for i in range( len(rows) / 2 ):
			achievement = Achievement()
			
			top_cols = rows[i].xpath('td')
			bottom_cols = rows[i + 1].xpath('td')

			if len(top_cols) == 3 and len(bottom_cols) == 2:
				achievement['game'] = game
				achievement['title'] = top_cols[1].xpath('a/b/text()').extract_first()
				achievement['artwork'] = top_cols[0].xpath('a/img/@src').extract_first()
				achievement['points'] = top_cols[2].xpath('strong/text()').extract_first()
				achievement['description'] = rows[i + 1].xpath('td/text()').extract_first()

				if achievement['title'] and achievement['artwork'] and achievement['points'] and achievement['description']:
					yield achievement
			
			