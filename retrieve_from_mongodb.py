from connect_to_mongodb import connect_to_mongo_db

client = connect_to_mongo_db()

db = client['used_cars']
collection = db['posting_details']

print(collection.find())

client.close()