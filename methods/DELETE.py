import enum
from databaseUser.HandlerDatabase import HandlerDatabase
from handler.HandlerErrors import HandlerErrors
from message.Request import Request
from message.Response import Response
from message.StatusCode import StatusCode


class DELETE:
    @staticmethod
    def response(request: Request) -> bytes:
        """ Performs a removal when there is a DELETE request, returning a response with
        the headers and the correct body. Removes the object within the database, based on the received ID.

        :param request: Request object, containing the body and headers of that request
        :returns: A byte object containing the response to this request

        """
        try:
            status: enum.Enum

            if request.URI != "/":
                pokemonID = DELETE.getIdOfUrl(request.URI)
                status = HandlerDatabase.deletePokemonByID(pokemonID)
            else:
                status = HandlerDatabase.deleteAllPokemons()

            header = {
                "Connection": "Closed",
            }
            if(int(status.value[0]) >= 400):
                return HandlerErrors.sendErrorCode(request, status)

            response = Response(status_code=status, body="", header=header)
            print("DELETE::response called " + request.URI + " -> " + status.value[1])
            return response.encodeResponse()
        except:
            print("DELETE::response called " + request.URI +  " -> BAD_REQUEST")
            return HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)

    @staticmethod
    def getIdOfUrl(URI: str) -> int:
        """ Return the id value present in the URL
    
        :param URI: String of the url
        :returns: The id value

        """
        if len(URI) > 5 and URI.rfind("/?id=") != -1:
            return URI[5: len(URI)]
        return -1
