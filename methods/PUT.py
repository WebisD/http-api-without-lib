from databaseUser.HandlerDatabase import HandlerDatabase
from databaseUser.ObjectUser import UserObj
from handler.HandlerErrors import HandlerErrors
from message.Response import Response
from message.StatusCode import StatusCode
import json


class PUT:
    @staticmethod
    def response(request):
        data = json.loads(request.body)

        idUrl = PUT.getIdOfUrl(request.URI)
        lastId = HandlerDatabase.getSizeList()

        if 0 <= idUrl <= lastId:
            if data['name'] != "" and data['phone'] != "" and data['pokemon'] != "" and data['image'] != "":
                obj = UserObj(data['name'], data['phone'], data['pokemon'], data['image'])
                # old obj -> based on index
                obj.setId(idUrl)

                status = HandlerDatabase.insertObj(obj)
                body = '<html><head></head><body><h1>Hello World<h1></body></html>'
                header = {
                    "Content-Length": "88",
                    "Content-Type": "text/html",
                    "Connection": "Closed",
                    "Last-Modified": "Wed, 22 Jul 2009 19:15:56 GMT"
                }
                response = Response(status_code=status, body=body, header=header)

                return response.encodeResponse()

        return HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)

    @staticmethod
    def getIdOfUrl(URI):
        if len(URI) > 5 and URI.rfind("/?id=") != -1:
            return int(URI[5: len(URI)])
        return -1
