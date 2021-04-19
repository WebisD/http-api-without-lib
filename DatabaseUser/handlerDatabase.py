from server import *
from threading import Thread
from Message.request import Request
from DatabaseUser.objectUser import UserObj
import json

class HandlerDatabase():
   databaseFile = 'DatabaseUser/database.json'
   database = {}

   @staticmethod
   def addNewObj(obj):
      try:
         with open(HandlerDatabase.databaseFile, 'r+') as file:
            HandlerDatabase.database = json.load(file)

            lastId = 0
            readObjs = HandlerDatabase.database["usersObj"]

            if len(readObjs) > 0:
               lastId = readObjs[len(readObjs) - 1]['id']

            value = {
               "id" : lastId + 1,
               "name" : obj.name,
               "phone": obj.phone,
               "pokemon" : obj.pokemon
            }

            HandlerDatabase.database["usersObj"].append(value)
            file.seek(0)
            json.dump(HandlerDatabase.database, file)
            return "200"
      except:
         return "500"