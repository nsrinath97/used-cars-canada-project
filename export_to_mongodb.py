from build_database import build_db_content
from connect_to_mongodb import connect_to_mongo_db

client = connect_to_mongo_db()

db = client['used_cars']
collection = db['posting_details']

used_cars_database = build_db_content()
collection.insert_many(used_cars_database)

client.close()