from databaseUser.HandlerDatabase import HandlerDatabase
from databaseUser.ObjectUser import UserObj
from handler.HandlerErrors import HandlerErrors
from message.Response import Response
from message.StatusCode import StatusCode
import json
import datetime

class PUT:
    @staticmethod
    def response(request) -> str:
        """ Performs an update when there is a PUT request, returning a response with
        the headers and the correct body. Updates the selected object within the database, based on the received ID.

        :param request: Request object, containing the body and headers of that request
        :returns: The answer to this request

        """
        try:
            requestData = json.loads(request.body)
            pokemonRequestData = list(requestData.values())[0]
            print(f"pokemonRequestData: {pokemonRequestData}")
            if pokemonRequestData["name"] != ""\
                    and pokemonRequestData["phone"] != ""\
                    and pokemonRequestData["pokemon"] != ""\
                    and pokemonRequestData["image"] != "":

                pokemonID = str(list(requestData.keys())[0])
                pokemonData = UserObj.fromDict(list(requestData.values())[0])
                pokemonData.setId(pokemonID)

                status = HandlerDatabase.updatePokemonByID(pokemonID, pokemonData)

                header = {
                    "Connection": "Closed"
                }
                response = Response(status_code=status, body=status.value[1], header=header)

                return response.encodeResponse()
            else:
                raise TypeError("Invalid data")
        except:
            return HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)

    @staticmethod
    def getIdOfUrl(URI) -> int:
        """ Return the id value present in the URL
    
        :param URI: String of the url
        :returns: The id value

        """
        if len(URI) > 5 and URI.rfind("/?id=") != -1:
            return int(URI[5: len(URI)])
        return -1
