from pymongo import MongoClient

# Local MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['studentportal']  # Replace with your database name

# Example of accessing a collection
collection = db['studentportal.login']  # Replace with your collection name

