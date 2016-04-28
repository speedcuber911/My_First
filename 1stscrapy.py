import scrapy
class dmoz(scrapy.Item):
    title = scrapy.Field();
    link = scrapy.Field();
    desc = scrapy.Field();
    
