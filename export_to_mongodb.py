from build_database import build_db_content
import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://nsrinath97:<password>@used-cars-vancouver.2tpj6or.mongodb.net/?retryWrites=true&w=majority')