from databaseUser.HandlerDatabase import HandlerDatabase
from databaseUser.ObjectUser import UserObj
from handler.HandlerErrors import HandlerErrors
from message.Response import Response
from message.StatusCode import StatusCode
import json


class POST:

    @staticmethod
    def parseRequestBody(request):
        parsedRequest: dict = {}
        elements = request.split('\n', 4)
        splitElem = []
        for elem in elements:
            splitElem.append(elem.split('=', 1))

        splitElem[4][1] = splitElem[4][1][:-1]

        parsedRequest = dict(splitElem[1:])

        return parsedRequest

    @staticmethod
    def response(request):
        try:
            data = json.loads(request.body)
            if data["name"] != "" and data["phone"] != "" and data["pokemon"] != "" and data["image"] != "":
                obj = UserObj(data['name'], data['phone'], data['pokemon'], data['image'])
                # new obj -> last index
                obj.setId(HandlerDatabase.getSizeList())

                status = HandlerDatabase.insertObj(obj)
                body = "<br><h2>Usuário adicionado com sucesso!<h2>" + f"<img src=\"{data['image']}\" style='object-fit: cover'  height=\"200\" /><br><br><br><br>"
                header = {
                    "Content-Length": f"{len(body)}",
                    "Content-Type": "text/html; charset=utf-8",
                    "Last-Modified": "Wed, 22 Jul 2009 19:15:56 GMT",
                    "Connection": "Closed"
                }
                response = Response(status_code=status, body=body, header=header)
                return response.encodeResponse()
            else:
                raise TypeError("Invalid data")
        except:
            return HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)
