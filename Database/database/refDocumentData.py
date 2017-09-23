import pymongo
from pprint import pprint
# from bson.dbref import DBRef
try:
    conn=pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e

db=conn.YNOS

cursor=(db.dealData.find({},{"InvestorID":1,"_id":0}))
invIds=[ids["InvestorID"] for ids in cursor]
print invIds
investorNames=(db.personData.find({"file_id":{"$in":invIds}},{"name":1,"_id":0}))

# investorNames=list(db.personData.find({"file_id":investorsIds[0]}))
print [invNames.values() for invNames in investorNames]
# for name in investorNames:
#     print name["name"]
#---------------- DBREF not working -------------------
# Link for info on referencing: https://gist.github.com/sbastn/769687

#
# for deal in db.dealData.find():
#     # Use each to iterate through an array
#     deal["InvestorID"]=DBRef(collection = "personData", id = db.personData.find_one({"file_id": deal["InvestorID"]}))
#     db.dealData.save(deal)
# cursor = db.dealData.InvestorID.id.find()

#------------------------------
# for cur in cursor:
#     print cur
# deals = db.dealData.find(modifiers={"$snapshot": True})
# for deal in deals:
#     print deal["InvestorID"],deal["startupName"]
#     db.dealData.update_one({"_id":deal["_id"]}, {"$set": {"InvestorID":{"$ref":"personData","$ID" :deal["InvestorID"],"$db":"YNOS"}}})
# for company in db.dealData.find():
#
#     invID = db.dealData.find_one({"startupName":company["startupName"]})['InvestorID']
#     # print invID
#     invName = db.personData.find({"file_id":invID})   # use $in to find the values in an array
#     # print invName
#     for name in invName:
#         print name['name']
#
#



    # pprint(db.dealData.find_one({"InvestorID":company["InvestorID"]})["startupName"])


# >var result = db.users.findOne({"name":"Tom Benzamin"},{"address_ids":1})
# >var addresses = db.address.find({"_id":{"$in":result["address_ids"]}})
# Using a query and a projector
# name = db.dealData.find({"startupName":"1CROWD"},{"InvestorName":1,"_id":0})