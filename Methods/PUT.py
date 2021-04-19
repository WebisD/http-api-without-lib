from Message.request import Request
from DatabaseUser.handlerDatabase import HandlerDatabase
from DatabaseUser.objectUser import UserObj
from Handler.handlerErrors import HandlerErrors
import json

class PUT():
    @staticmethod
    def response(request):
        data = json.loads(request.body)

        idUrl = PUT.getIdOfUrl(request.URI)
        lastId = HandlerDatabase.getSizeList()

        if idUrl >= 0 and idUrl <= lastId:
            if data['name'] != "" and data['phone'] != "" and data['pokemon'] != "":
                obj = UserObj(data['name'], data['phone'], data['pokemon'])
                #old obj -> based on index
                obj.setId(idUrl)
                status = HandlerDatabase.insertObj(obj)
                return status.encode()

        return HandlerErrors.sendErrorCode(request)

    @staticmethod
    def getIdOfUrl(URI):
        if(len(URI) > 5 and URI.rfind("/?id=") != -1):
            return int(URI[5: len(URI)])
        return -1