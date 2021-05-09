import datetime
from databaseUser.HandlerDatabase import HandlerDatabase
from databaseUser.ObjectUser import UserObj
from handler.HandlerErrors import HandlerErrors
from message.Response import Response
from message.StatusCode import StatusCode
import json

class POST:

    @staticmethod
    def response(request) -> str:
        """ Performs an insertion when there is a POST request, returning a response with
        the headers and the correct body. Adds the received object within the database.

        :param request: Request object, containing the body and headers of that request
        :returns: The answer to this request

        """
        try:
            data = json.loads(request.body)
            if data["name"] != "" and data["phone"] != "" and data["pokemon"] != "" and data["image"] != "" and data["image"] != "http://localhost:8083/post":
                obj = UserObj.fromDict(data)

                obj.setId(datetime.datetime.now().strftime("%d%m%Y%H%M%S"))

                status = HandlerDatabase.insertPokemon(obj)
                header = {
                    "Connection": "Closed"
                }
                if(int(status.value[0]) >= 400):
                    return HandlerErrors.sendErrorCode(request, status)

                response = Response(status_code=status, body=status.value[1], header=header)
                print("POST::response called " + request.URI + " -> " + status.value[1])

                return response.encodeResponse()
            else:
                raise TypeError("Invalid data")
        except Exception as e:
            print(e)
            print("POST::response called " + request.URI +  " -> BAD_REQUEST")
            return HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)
