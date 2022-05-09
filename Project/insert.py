from datetime import datetime
import pandas as pd                                                     
from pymongo import MongoClient
try:
    conn = MongoClient("mongodb://172.31.17.147:27021")
    print("connected")
except:
    print("not connected")
db = conn.moviesDB
df = pd.read_csv('tags.csv')

li =[]
for index, row in df.iterrows():
    insertValue ={
        "userId" : row['userId'],
        "movieId" : row['movieId'],
        "tag" : row['tag'],
        "timestamp" : datetime.fromtimestamp(row['timestamp'])
        }
    collection = db.tags
    insertRes = collection.insert_one(insertValue)
    print("Inserted this value", insertRes)
