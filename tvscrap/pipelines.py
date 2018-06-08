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
        self.cur.execute("DELETE FROM tvShowepisodes WHERE network = %s;", (item['tv_network']))

    def closer_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        # You have to import tv_networks database yourself so foreign key works
        self.cur.execute("INSERT INTO tvShowepisodes(tv_title, tv_intro, tv_name,
                         tv_link, tv_img, tv_epi_num, network) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                         (item['tv_title'], item['tv_intro'],item['tv_name'],
                          item['tv_link'],item['tv_img'],item['tv_episode_number'],
                          item['tv_network']))
        self.cur.commit()
        return item
