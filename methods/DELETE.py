import enum
from databaseUser.HandlerDatabase import HandlerDatabase
from message.Response import Response
from message.StatusCode import StatusCode

class DELETE:
    @staticmethod
    def response(request):
        try:
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
            if(int(status.value[0]) >= 400):
                return HandlerErrors.sendErrorCode(request, status)

            response = Response(status_code=status, body="", header=header)
            return response.encodeResponse()
        except:
            return HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)

    @staticmethod
    def getIdOfUrl(URI):
        if len(URI) > 5 and URI.rfind("/?id=") != -1:
            return URI[5: len(URI)]
        return -1
