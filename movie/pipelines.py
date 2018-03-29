# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from mysqlUtils import dbhandle_online


class MoviePipeline(object):
    def process_item(self, item, spider):
#         with open(".\my_meiju.txt",'a') as fp:
#             #fp.write(item['name'].encode("utf8"))
#             fp.write(item['name']+'\n')

            db_object = dbhandle_online()
            cursor = db_object.cursor()
            sql = 'insert into dg_spider.dg_spider_post(title) ' \
            'values("%s")' \
            % (item['name'])
            try:
                cursor.execute(sql)
                #cursor.fetchone()
                db_object.commit()            
            except Exception as e:
                print(item['name'])
                print("catch exception")     
                print(e)

            cursor.close()
            db_object.close()

            