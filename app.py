from flask import Flask, render_template
from connect_to_mongodb import connect_to_mongo_db

app = Flask(__name__)   # Initialize Flask


@app.route("/") # Homepage of website
def home():
    client = connect_to_mongo_db()  # Connect to mongoDB database
    db = client['used_cars']    # Extract database from MongoDB
    collection = db['posting_details']  # Extract collection from database

    # Put the collection into a list of documents in JSON format
    table_rows = []
    for row in collection.find():
        table_rows.append(row)

    # returns the html file for the website
    return render_template("index.html", vehicles_table=table_rows)


if __name__ == "__main__":
    app.run()
