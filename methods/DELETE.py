import enum
from databaseUser.HandlerDatabase import HandlerDatabase
from message.Response import Response
from message.StatusCode import StatusCode

class DELETE:
    @staticmethod
    def response(request):
        status: enum.Enum

        if request.URI != "/":
            pokemonID = DELETE.getIdOfUrl(request.URI)
            print(f"Delete PokemonID: {pokemonID}")
            status = HandlerDatabase.deletePokemonByID(pokemonID)
        else:
            status = HandlerDatabase.deleteAllPokemons()

        header = {
            "Connection": "Closed",
        }

        response = Response(status_code=status, body="", header=header)
        return response.encodeResponse()

    @staticmethod
    def getIdOfUrl(URI):
        if len(URI) > 5 and URI.rfind("/?id=") != -1:
            return URI[5: len(URI)]
        return -1
