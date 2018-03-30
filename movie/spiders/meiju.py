# -*- coding: utf-8 -*-
import scrapy
import json
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    #allowed_domains = ['meijutt.com']
    #start_urls = ['http://meijutt.com/new100.html']
    allowed_domains = ['stock2.finance.sina.com.cn']
    start_urls = ['http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine15m?symbol=RB0']
    def parse(self, response):
        #movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        movies = json.loads(response.body)
        print(response.body)
        main_data = json.loads(response.body.decode("utf-8"))
        for eveData in main_data:
            item = MovieItem()
            item['name'] = eveData
            print(item['name'])
            yield item
        #for each_movie in movies:
            #item = MovieItem()
            #item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            #item['name'] = each_movie   
            #yield item
