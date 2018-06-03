# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
import databaseNameSpace

class TvscrapPipeline(object):
    def open_spider(self, spider):
        hostname = databaseNameSpace.DatabaseName['hostname']
        username = databaseNameSpace.DatabaseName['username']
        password = databaseNameSpace.DatabaseName['password']
        database = databaseNameSpace.DatabaseName['database']
        self.connection = psycopg2.connect(host=hostname, user=username,
                                           password=password, dbname=database)
        self.cur = self.connection.cursor()

    def closer_spider(self, spider):
        self.cur.close()
        self.connection.close()
        
    def process_item(self, item, spider):
        return item
