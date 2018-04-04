# -*- coding: utf-8 -*-
# @Time : 2017/1/1 17:51
# @Author : woodenrobot

from scrapy.crawler import CrawlerProcess
from spiders.meiju import MeijuSpider
import scrapy.utils.project 
from sys import stdin

print ("init...")
spider = MeijuSpider()
setttings = scrapy.utils.project.get_project_settings()
process = CrawlerProcess(setttings)
process.crawl(spider)
process.start()
x = stdin.read(1)



def run_spider():
    print ("init...")
    spider = MeijuSpider()
    setttings = scrapy.utils.project.get_project_settings()
    process = CrawlerProcess(setttings)
    process.crawl(spider)
    process.start()
    x = stdin.read(1)
