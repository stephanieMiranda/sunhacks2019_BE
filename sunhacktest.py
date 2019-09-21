import pymongo
from pprint import pprint
client = pymongo.MongoClient("mongodb+srv://SunhacksAR:temp01@sunhacks2019-rmmqb.mongodb.net/test?retryWrites=true&w=majority")
db = client["sunhacks"]

#db.get_collection("Users")
Users = db["Users"]
print(Users.find_one({"Name":"Jacob"}))
print("------------------------------")
pprint(Users.find_one({"Name":"Jacob"}))

def getUserById():

def getEventById():

def getSponsorById():

def getUserByEmail():

def getEventByNameDate():

def getSponsorByName():

def addUser():

def addSponsor():

def addEvent():