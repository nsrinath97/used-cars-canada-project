from connect_to_mongodb import connect_to_mongo_db

client = connect_to_mongo_db() # connect to mongodb client

# Select the database and collection where to insert documents
db = client['used_cars']
collection = db['posting_details']

# Grabs the all the rows in the collection
table_rows = []
for row in collection.find():
    table_rows.append(row)

client.close()