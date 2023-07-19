from flask import Flask, render_template
from connect_to_mongodb import connect_to_mongo_db

app = Flask(__name__)


@app.route("/")
def home():
    client = connect_to_mongo_db()
    db = client['used_cars']
    collection = db['posting_details']

    table_rows = []
    for row in collection.find():
        table_rows.append(row)

    return render_template("index.html", vehicles_table=table_rows)


if __name__ == "__main__":
    app.run()
