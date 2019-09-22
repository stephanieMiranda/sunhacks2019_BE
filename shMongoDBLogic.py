import pymongo
from pprint import pprint
#create mongo client
client = pymongo.MongoClient("mongodb+srv://SunhacksAR:temp01@sunhacks2019-rmmqb.mongodb.net/test?retryWrites=true&w=majority")
#set db to use, in this case we're using a generic name for the sunhack project
db = client["sunhacks"]
#the two documents we're using, Users, and Company
users = db["Users"]
company = db["Company"]
class ShMongoDBLogic:
    __db = None
    @classmethod
    def get_connection(cls):
        if cls.__db is None:
            cls.__db = Connection()
        return cls.__db

    #return a user document from the users database document if the user exists
    @classmethod
    def getUserByEmail(self, email):
        userDoc = users.find_one({"Email":email})
        if(userDoc == None):
            return False
        else:
            return userDoc

    #return a company document from the company database document if the company exists
    @classmethod
    def getCompanyByName(self, name):
        comDoc = company.find_one({"Name":name})
        if(comDoc == None):
            return False
        else:
            return comDoc

    #If user does not exist, add user, else print to console and return email of user
    @classmethod
    def addUser(name, email, color, power, field, hobby):
        if(getUserByEmail(email) == False):
            print("Not found")
            newUser = [{"Name" : name, 
                "Email" : email,
                "Favorite_Color" : color,
                "Superpower" : power,
                "Field" : field,
                "Favorite_Hobby" : hobby,
                "Nametag" : email + ".nametag"
                }]
            users.insert_one(newUser)
            return True
        else:
            print("User already exists")
            return email

    #If company does not exist, add comapny, else print to console and return name of comapny
    @classmethod
    def addCompany(name, rep, repField, mission, recruit):
        if(getCompanyByName(name) == False):  
            newComp = [{"Name" : name,
                "Rep" : rep,
                "Rep_Field" : repField,
                "Mission" : mission,
                "Recruiting" : recruit
            }]
            company.insert_one(newComp)
            return True
        else:
            print("Company already exists")
            return name
            
    def addTheTeam():
        addUser('Mason Cole', 'mcole18@asu.edu', '42a881', 'teleportation', 'software engineering', 'complaining')
        addUser('Jon Bartlett', 'jtbartl2@asu.edu', '42a881', 'flight', 'software engineering', 'Soccer')
        addUser('Stephanie Miranda', 'smirand6@asu.edu', '425caa', 'levitation', 'software engineering', 'doodling')

    #addTheTeam()

    def getTesting():
        print(users.find_one({"Name":"Jacob Wallert"}))
        print("------------------------------")
        userDoc = ShMongoDBLogic.getUserByEmail("jawaller@asu.edu")
        comDoc = ShMongoDBLogic.getCompanyByName("State Farm")
        print("User information for " + userDoc["Name"] + ":")
        print("------------------------------")
        pprint(userDoc)
        print("------------------------------")
        print(comDoc["Name"] +" company information:")
        print("------------------------------")
        pprint(comDoc)
        print("------------------------------")
        pprint(ShMongoDBLogic.getUserByEmail("mcole18@asu.edu"))
        
    def addTesting():
        #new adds
        addCompany("Amazon","John Doe","System Engineer", "The mission and vision of Amazon.com is: Our vision is to be earth's most customer-centric company; to build a place where people can come to find and discover anything they might want to buy online.",["Software Engineering", "Electrical Engineering"])
        addUser("Paul Jones", "test@donut.org", "C20D49", "Eating", "Chef", "Cooking")
        print(getCompanyByName("Amazon"))
        print("Should be two True prints:")
        print(getUserByEmail("test@donut.org") != False)
        print(getCompanyByName("Amazon") != False)
        #trying to add existing
        addCompany("Amazon","John Doe","System Engineer", "The mission and vision of Amazon.com is: Our vision is to be earth's most customer-centric company; to build a place where people can come to find and discover anything they might want to buy online.",["Software Engineering", "Electrical Engineering"])
        addUser("Paul Jones", "test@donut.org", "C20D49", "Eating", "Chef", "Cooking")
        users.delete_one({"Email":"test@donut.org"})
        company.delete_one({"Name":"Amazon"})
        print("Should be two False prints:")
        print(getUserByEmail("test@donut.org")  != False)
        print(getCompanyByName("Amazon")  != False)
    #uncomment to test gets    
    #getTesting()
    #uncomment to test adds
    #addTesting()

ShMongoDBLogic.getTesting()