# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class DineoutPipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect("Restaurants.db")
        self.c = self.connection.cursor()
        self.c.execute('''
            CREATE TABLE restaurant (
            Name TEXT,
            Cuisine TEXT,
            Type TEXT,
            Cost TEXT,
            Facilities TEXT,
            Rating TEXT,
            Votes TEXT,
            Reviews TEXT,
            Location TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO restaurant (Name,Cuisine,Type,Cost,Facilities,Rating,Votes,Reviews,Location) VALUES (?,?,?,?,?,?,?,?,?)
        ''',(
                item.get('Name'),
                item.get('Cuisine'),
                item.get('Type'),
                item.get('Cost'),
                item.get('Facilities'),
                item.get('Rating'),
                item.get('Votes'),
                item.get('Reviews'),
                item.get('Location')
        ))
        self.connection.commit()
        return item
