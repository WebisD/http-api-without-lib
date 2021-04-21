from databaseUser.HandlerDatabase import HandlerDatabase
from databaseUser.ObjectUser import UserObj
from handler.HandlerErrors import HandlerErrors
from message.Response import Response
from message.StatusCode import StatusCode
import json


class POST:
    @staticmethod
    def response(request):
        data = json.loads(request.body)
        if data['name'] != "" and data['phone'] != "" and data['pokemon'] != "" and data['image'] != "":
            obj = UserObj(data['name'], data['phone'], data['pokemon'], data['image'])
            # new obj -> last index
            obj.setId(HandlerDatabase.getSizeList())

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
