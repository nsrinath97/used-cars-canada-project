from build_database import build_db_content
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect_to_mongo_db():

    MONGO_DB_PASS = os.environ['MONGO_DB_PASS']

    uri = "mongodb+srv://nsrinath97:" + MONGO_DB_PASS + "@used-cars-vancouver.2tpj6or.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client

client = connect_to_mongo_db()

db = client['used_cars']
collection = db['posting_details']

used_cars_database = build_db_content()
collection.insert_many(used_cars_database)

client.close()