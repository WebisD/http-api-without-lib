from databaseUser.HandlerDatabase import HandlerDatabase
from databaseUser.ObjectUser import UserObj
from handler.HandlerErrors import HandlerErrors
from message.Response import Response
import json


class PUT:
    @staticmethod
    def response(request):
        data = json.loads(request.body)

        idUrl = PUT.getIdOfUrl(request.URI)
        lastId = HandlerDatabase.getSizeList()

        if 0 <= idUrl <= lastId:
            if data['name'] != "" and data['phone'] != "" and data['pokemon'] != "":
                obj = UserObj(data['name'], data['phone'], data['pokemon'])
                # old obj -> based on index
                obj.setId(idUrl)

                status = HandlerDatabase.insertObj(obj)
                lastMod = 'Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT'
                body = '<html><head></head><body><h1>Hello World<h1></body></html>'
                header = {
                    "Content-Length": "88",
                    "Content-Type": "text/html",
                    "Connection": "Closed"
                }
                response = Response(status_code=status, last_modified=lastMod, body=body, header=header)

                return response.sendResponse()

        return HandlerErrors.sendErrorCode(request)

    @staticmethod
    def getIdOfUrl(URI):
        if len(URI) > 5 and URI.rfind("/?id=") != -1:
            return int(URI[5: len(URI)])
        return -1
