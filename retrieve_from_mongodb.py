from connect_to_mongodb import connect_to_mongo_db

client = connect_to_mongo_db()

db = client['used_cars']
collection = db['posting_details']

table_rows = []
for row in collection.find():
    table_rows.append(row)

client.close()