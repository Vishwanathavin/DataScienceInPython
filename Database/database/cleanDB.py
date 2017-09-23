import pymongo

dbName = 'YNOS'
collectionName = ['dealData','personData']

try:
    conn=pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e

db = conn[dbName]
for col in collectionName:
    db[col].drop()
