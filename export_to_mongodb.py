from build_database import build_db_content
from connect_to_mongodb import connect_to_mongo_db


used_cars_database = build_db_content() # Runs the build_db_content file to create a list of post details

client = connect_to_mongo_db()  # connect to mongodb client

# Select the database and collection where to insert documents
db = client['used_cars']
collection = db['posting_details'] 

collection.insert_many(used_cars_database) # inserts the posts in the form of JSON documents

client.close()