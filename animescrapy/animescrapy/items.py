# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeScrapyItem(scrapy.Item):
    id = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    listStatus = scrapy.Field()
    mediaType = scrapy.Field()
    numEpisodes = scrapy.Field()
    score = scrapy.Field()
    numListUsers = scrapy.Field()
    status = scrapy.Field()
