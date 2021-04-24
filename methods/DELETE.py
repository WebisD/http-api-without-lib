import enum
from databaseUser.HandlerDatabase import HandlerDatabase
from message.Response import Response


class DELETE:
    @staticmethod
    def response(request):
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
    def getIdOfUrl(URI):
        if len(URI) > 5 and URI.rfind("/?id=") != -1:
            return URI[5: len(URI)]
        return -1
