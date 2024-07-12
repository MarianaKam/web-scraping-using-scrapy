# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        return item

# import psycopg2

# def __init__(self):
#     hostname = 'localhost'
#     username = 'postgres'
#     password = '123456'
#     database = 'postgres'

#     self.connection = psycopg2.connect(host=hostname, user=username, password=password,)
