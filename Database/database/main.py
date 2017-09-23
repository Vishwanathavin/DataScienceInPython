import pymongo
import json
import pandas as pd
















# Checking if they can be accessed from one another


# Add validator


# Indexing
# pprint(db.collection_names())
# db.myCollection.insert(records)

# collection = db.test_collection
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#             "date": datetime.datetime.utcnow()}
# post_id = db.test_collection.insert_one(post).inserted_id
# print post_id
# new_posts = [{"author": "Mike",
#               "text": "Another post!",
#               "tags": ["bulk", "insert"],
#               "date": datetime.datetime(2009, 11, 12, 11, 14)},
#              {"author": "Eliot",
#               "title": "MongoDB is fun",
#               "text": "and pretty easy too!",
#               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
# result = db.test_collection.insert_many(new_posts)
# d = datetime.datetime(2009, 11, 12, 12)
# for post in db.test_collection.find({"$and":[{"author": "Mike"},{"date":{"$lt":d}}]}):
# for post in db.test_collection.find({"date":{"$lt":d}}).sort("author"):
# for post in db.test_collection.find():
#     pprint.pprint(db.test_collection.find_one(post))


# pprint.pprint(db.test_collection.find_one({"_id":ObjectId("59ba416edc53fd1d1008f9a7")}))

# result = db.profiles.create_index([('user_id', ASCENDING)],
#                                   unique=True)
# pprint.pprint(((db.profiles.index_information())))

# user_profiles = [
#    {'user_id': 211, 'name': 'Luke'},
#      {'user_id': 212, 'name': 'Ziltoid'}]
# result = db.profiles.insert_many(user_profiles)
# pprint.pprint(db.myCollection.count())

