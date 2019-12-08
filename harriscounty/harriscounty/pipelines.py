# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from elasticsearch import Elasticsearch

class HarriscountyPipeline(object):

    def __init__(self):
        self.es = None
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        if self.es.ping():
            print('Yay Connect')
        else:
            print('Awww it could not connect!')

        self.index_name = 'testsites'
        # index settings
        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            },
            "mappings": {
                'testsites': {
                    "properties": {
                        "url": {
                            "type": "text"
                        },
                        "text": {
                            "type": "text"
                        }
                    }
                }
            }
        }

        try:
            if not self.es.indices.exists(self.index_name):
                # Ignore 400 means to ignore "Index Already Exist" error.
                self.es.indices.create(index=self.index_name, ignore=400, body=settings)
                print('Created Index')
        except Exception as ex:
            print(str(ex))
        finally:
            print('Created Index')

        

    def process_item(self, item, spider):
        # print(type(dict(item)))
        try:
            outcome = self.es.index(index=self.index_name, doc_type='urls', body=dict(item))
            print(outcome)
        except Exception as ex:
            print('Error in indexing data')
            print(str(ex))
        finally:
            return item