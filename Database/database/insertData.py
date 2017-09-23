import pymongo
import json
import pandas as pd
from pprint import pprint

startupFile = pd.read_csv('./startupData.csv')
personFile = pd.read_csv('./personData.csv')
# startupFile=startupFile.encode('ascii', 'ignore')
# personFile=personFile.encode('ascii', 'ignore')
try:
    conn=pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e

db=conn.YNOS

# insert both the collections
records = json.loads(startupFile.T.to_json()).values()
db.dealData.insert(records)

records = json.loads(personFile.T.to_json()).values()
db.personData.insert(records)


print "Done inserting data"