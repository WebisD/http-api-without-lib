import datetime
from databaseUser.HandlerDatabase import HandlerDatabase
from databaseUser.ObjectUser import UserObj
from handler.HandlerErrors import HandlerErrors
from message.Response import Response
from message.StatusCode import StatusCode
import json


class POST:

    @staticmethod
    def response(request):
        try:
            data = json.loads(request.body)
            if data["name"] != "" and data["phone"] != "" and data["pokemon"] != "" and data["image"] != "" and data["image"] != "http://localhost:8080/post":
                obj = UserObj.fromDict(data)

                print("POST" + str(obj))

                obj.setId(datetime.datetime.now().strftime("%d%m%Y%H%M%S"))

                status = HandlerDatabase.insertPokemon(obj)
                header = {
                    "Connection": "Closed"
                }
                if(int(status.value[0]) >= 400):
                    return HandlerErrors.sendErrorCode(request, status)

                response = Response(status_code=status, body=status.value[1], header=header)

                return response.encodeResponse()
            else:
                raise TypeError("Invalid data")
        except Exception as e:
            print(e)
            return HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)
