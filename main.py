import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://findThief:findThief@cluster0.sqm88.mongodb.net/?retryWrites=true&w=majority")
db = client.demo
coll = db.vsDemo
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
documents = coll.find()
for doc in documents:
    description = doc.get("description")
    if description:
        vector = model.encode(description)
        coll.update_one({"_id": doc["_id"]}, {"$set": {"descriptionVector": vector.tolist()}})

