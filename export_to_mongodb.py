from build_database import build_db_content
import pymongo
from pymongo import MongoClient
import os

MONGO_DB_PASS = os.environ['MONGO_DB_PASS']

cluster = MongoClient('mongodb+srv://nsrinath97:'+ MONGO_DB_PASS +'@used-cars-vancouver.2tpj6or.mongodb.net/?retryWrites=true&w=majority')

db = cluster['used_cars']
collection = db['posting_details']

used_cars_database = build_db_content()

collection.insert_many(used_cars_database)

cluster.close()