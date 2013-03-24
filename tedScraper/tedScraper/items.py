# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class tedTalk(Item):
    title = Field()
    speaker = Field()
    duration = Field()
    datePublished = Field()
    eventName = Field()
    ShortSummary = Field()
    url = Field()
    rankings = Field()
    transcript = Field()
    
