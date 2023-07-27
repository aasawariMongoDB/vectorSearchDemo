import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://findThief:findThief@cluster0.sqm88.mongodb.net/?retryWrites=true&w=majority")
db = client.demo
coll = db.vsDemo
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# sample Queries
#query = "provides efficient transport access"
#query = "Has place to stay nearby"
#query = "has public transport available"
query = "There are no house rules"

encoded_query = model.encode(query).tolist()
pipeline = [
    {
        "$search": {
            "index": "demoIndex",
            "knnBeta": {
                "vector": encoded_query,
                "path": "descriptionVector",
                "k": 5
            }
        }
    }
]
results = coll.aggregate(pipeline)
for fetched_doc in results:
    print(fetched_doc["description"])
