from server import *
from threading import Thread
from message.Request import Request
from databaseUser.ObjectUser import UserObj
from message.StatusCode import StatusCode
import json
import numpy as np

class HandlerDatabase:
    databaseFile = 'databaseUser/database.json'
    database = {}

    @staticmethod
    def insertObj(obj):
        try:
            with open(HandlerDatabase.databaseFile, 'r+') as file:
                HandlerDatabase.database = json.load(file)

                value = {
                    "id": obj.id,
                    "name": obj.name,
                    "phone": obj.phone,
                    "pokemon": obj.pokemon,
                    "image": obj.image
                }

                # new obj
                if obj.id == HandlerDatabase.getSizeList():
                    HandlerDatabase.database["usersObj"].append(value)
                # update obj
                else:
                    HandlerDatabase.database["usersObj"][obj.id] = value

                file.seek(0)
                json.dump(HandlerDatabase.database, file, indent=4)
                file.truncate()
                return StatusCode.OK
        except:
            return StatusCode.INTERNAL_SERVER_ERROR

    @staticmethod
    def deleteObj(id):
        try:
            with open(HandlerDatabase.databaseFile, 'r+') as file:
                HandlerDatabase.database = json.load(file)
                print("AAAAAa")

                status = StatusCode.OK
                idIterator = 0
                for obj in HandlerDatabase.database["usersObj"]:
                    if obj['id'] == id:
                        HandlerDatabase.database["usersObj"].pop(idIterator)
                        break
                    idIterator+=1
               
                file.seek(0)
                json.dump(HandlerDatabase.database, file, indent=4)
                file.truncate()
                return status
        except:
            return StatusCode.INTERNAL_SERVER_ERROR

    @staticmethod
    def deleteAllObj():
        try:
            with open(HandlerDatabase.databaseFile, 'r+') as file:
                HandlerDatabase.database = json.load(file)

                status = StatusCode.OK
                if not HandlerDatabase.database["usersObj"]:
                    status = StatusCode.NOT_MODIFIED
                HandlerDatabase.database["usersObj"] = []

                file.seek(0)
                json.dump(HandlerDatabase.database, file, indent=4)
                file.truncate()
                return StatusCode.OK
        except:
            return StatusCode.INTERNAL_SERVER_ERROR

    @staticmethod
    def getSizeList():
        try:
            with open(HandlerDatabase.databaseFile, 'r+') as file:
                HandlerDatabase.database = json.load(file)
                size = len(HandlerDatabase.database["usersObj"])
                lastId = HandlerDatabase.database["usersObj"][size - 1]['id']
                return int(lastId + 1)

        except:
            return int(-1)
