import scrapy


class Game(scrapy.Item):
	kind = scrapy.Field()
	title = scrapy.Field()
	artwork = scrapy.Field()
	achievement_count = scrapy.Field()
	achievement_list_url = scrapy.Field()


class Achievement(scrapy.Item):
	kind = scrapy.Field()
	game = scrapy.Field()
	title = scrapy.Field()
	artwork = scrapy.Field()
	points = scrapy.Field()
	description = scrapy.Field()
