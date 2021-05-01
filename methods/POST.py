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
            if data["name"] != "" and data["phone"] != "" and data["pokemon"] != "" and data["image"] != "":
                obj = UserObj.fromDict(data)

                obj.setId(datetime.datetime.now().strftime("%d%m%Y%H%M%S"))
                print(datetime.datetime.now().strftime("%d%m%Y%H%M%S"))

                status = HandlerDatabase.insertPokemon(obj)
                print(status)

                header = {
                    "Connection": "Closed"
                }

                response = Response(status_code=status, body=status.value[1], header=header)

                return response.encodeResponse()
            else:
                raise TypeError("Invalid data")
        except:
            return HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)
