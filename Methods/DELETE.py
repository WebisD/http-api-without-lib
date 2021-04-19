from Message.request import Request
from DatabaseUser.handlerDatabase import HandlerDatabase
from DatabaseUser.objectUser import UserObj
from Handler.handlerErrors import HandlerErrors
import json

class DELETE():
    @staticmethod
    def response(request):
        data = json.loads(request.body)

        if(request.URI != "/"):
            idUrl = DELETE.getIdOfUrl(request.URI)
            lastId = HandlerDatabase.getSizeList()

            if idUrl >= 0 and idUrl <= lastId:
                status = HandlerDatabase.deleteObj(idUrl)
                return status.encode()
        else:
            status = HandlerDatabase.deleteAllObj()
            return status.encode()

        return HandlerErrors.sendErrorCode(request)

    @staticmethod
    def getIdOfUrl(URI):
        if(len(URI) > 5 and URI.rfind("/?id=") != -1):
            return int(URI[5: len(URI)])
        return -1