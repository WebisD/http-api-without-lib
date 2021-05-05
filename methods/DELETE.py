import enum
from databaseUser.HandlerDatabase import HandlerDatabase
from message.Response import Response

class DELETE:
    @staticmethod
    def response(request) -> str:
        """ Performs a removal when there is a DELETE request, returning a response with
        the headers and the correct body. Removes the object within the database, based on the received ID.

        :param request: Request object, containing the body and headers of that request
        :returns: The answer to this request

        """
        print("DELETE::response called")
        status: enum.Enum

        print(f"URL: {request.URI}\n"
              f"body: {request.body}")

        if request.URI != "/":
            pokemonID = DELETE.getIdOfUrl(request.URI)
            print(f"PokemonID: {pokemonID}")
            status = HandlerDatabase.deletePokemonByID(pokemonID)
        else:
            status = HandlerDatabase.deleteAllPokemons()

        header = {
            "Connection": "Closed",
        }

        print(f"Status: {status.value[0]}")
        print()
        response = Response(status_code=status, body="", header=header)
        return response.encodeResponse()

    @staticmethod
    def getIdOfUrl(URI) -> int:
        """ Return the id value present in the URL
    
        :param URI: String of the url
        :returns: The id value

        """
        if len(URI) > 5 and URI.rfind("/?id=") != -1:
            return URI[5: len(URI)]
        return -1
