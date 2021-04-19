from server import *
from threading import Thread
from Message.request import Request
from DatabaseUser.objectUser import UserObj
import json

class HandlerDatabase():
   databaseFile = 'DatabaseUser/database.json'
   database = {}

   @staticmethod
   def insertObj(obj):
      try:
         with open(HandlerDatabase.databaseFile, 'r+') as file:
            HandlerDatabase.database = json.load(file)
            
            value = {
               "id" : obj.id,
               "name" : obj.name,
               "phone": obj.phone,
               "pokemon" : obj.pokemon
            }

            #new obj
            if obj.id == HandlerDatabase.getSizeList():
                  HandlerDatabase.database["usersObj"].append(value)
            #update obj
            else:
               HandlerDatabase.database["usersObj"][obj.id] = value

            file.seek(0)
            json.dump(HandlerDatabase.database, file, indent=4)
            file.truncate() 
            return "200"
      except:
         return "500"
      
   @staticmethod
   def getSizeList():
      try:
         with open(HandlerDatabase.databaseFile, 'r+') as file:
            HandlerDatabase.database = json.load(file)
            return int(len(HandlerDatabase.database["usersObj"]))
           
      except:
         return int(-1)