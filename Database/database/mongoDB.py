import pandas as pd
import pymongo
import json
from pprint import pprint
from bson.objectid import ObjectId
def dataTODB():
   inpFile = pd.read_csv('../Data/startupData.csv')

   client = pymongo.MongoClient()

   db=client.test_database
   # db.create_collection('dealData')
   # db.create_collection('personData')


   records = json.loads(inpFile.T.to_json()).values()
   db.startupData.insert(records)
   # db.myCollection.insert_one({"startupName":"deTect","City": "Chennai"})

   # for post in db.myCollection.find():
   #     pprint(db.myCollection.find_one(post))


def main():
    dataTODB()
if __name__=='__main__':
    main()


# Comments
# Initialize IDS
   # productID=ObjectId()
   # customerID=ObjectId()

   # db.dealData.insert_one({"_id":productID,"product":"kannadi","customerID":customerID})
   # db.personData.insert_one({"_id":customerID,"name":"radhi","Place":"Chennai"})