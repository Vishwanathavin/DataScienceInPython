from pymongo import MongoClient
client = MongoClient()
db = client.test

#Insert JSON
# mongoimport --db test --collection restaurants --drop --file ~/downloads/primer-dataset.json

# Insert command: returns object ID
from datetime import datetime
# result = db.restaurants.insert_one(
#     {
#         "address": {
#             "street": "2 Avenue",
#             "zipcode": "10075",
#             "building": "1480",
#             "coord": [-73.9557413, 40.7720266]
#         },
#         "borough": "Manhattan",
#         "cuisine": "Italian",
#         "grades": [
#             {
#                 "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
#                 "grade": "A",
#                 "score": 11
#             },
#             {
#                 "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
#                 "grade": "B",
#                 "score": 17
#             }
#         ],
#         "name": "Vella",
#         "restaurant_id": "41704620"
#     }
# )
# print result.inserted_id

#Find - returns cursor object
# cursor = db.restaurants.find({"grades.grade": {"$all": ["A", "B"]}})
# cursor = db.restaurants.find({"grades.score": {"$gt": 30}})
# cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})
# for document in cursor:
#     print(document)

result = db.restaurants.update_one(
    {"name": "Juni"},
    {
        "$set": {
            "cuisine": "American (New)"
        },
        "$currentDate": {"lastModified": True}
    }
)

print result.matched_count