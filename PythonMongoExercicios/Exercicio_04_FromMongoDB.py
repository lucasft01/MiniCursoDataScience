
import csv
from pymongo import MongoClient

def csv_to_json(db_name, collection_name, csv_file):
    #CSV to JSON Conversion
    Client = MongoClient()
    db = Client[db_name] 
    collection = db[collection_name]
    
    with open(csv_file, "rt") as infile:
        reader = csv.DictReader(infile)
        next(reader)
        for each in reader:
            collection.insert_one(each)

db_name = "GECID3"
collection_name = "Hepatitis"
csv_file = "/home/lucasft/Downloads/MiniCurso/PythonExercicios/hepatitis.csv"
csv_to_json(db_name, collection_name, csv_file)
