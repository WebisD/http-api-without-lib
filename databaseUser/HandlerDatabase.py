from message.StatusCode import StatusCode
import json
from databaseUser.ObjectUser import UserObj
from handler.HandlerImage import HandlerImage
import pathlib

class HandlerDatabase:
    pokemonDatabasePath: str = 'databaseUser/database.json'
    pokemonDatabase: dict = {}

    @staticmethod
    def insertPokemon(obj: UserObj):
        database: dict = HandlerDatabase.getData()

        if database is None:
            return StatusCode.INTERNAL_SERVER_ERROR

        pokemonID = obj.id
        HandlerImage.saveImg(obj)

        extensionImage = pathlib.Path(obj.image).suffix
        urlImage = "/" + obj.id +  extensionImage

        pokemonData = {
            "name": obj.name,
            "phone": obj.phone,
            "pokemon": obj.pokemon,
            "image": urlImage
        }
        try:
            HandlerImage.addLinkImage(urlImage, extensionImage)
        except:
            print("erro in link image")
        
        isPokemonRegistered, pokemonIndex = HandlerDatabase.isPokemonRegistered(pokemonID)
        if isPokemonRegistered:
            database["users"][pokemonIndex] = pokemonData
        else:
            database["users"].append({pokemonID: pokemonData})

        if HandlerDatabase.setData(database):
            return StatusCode.CREATED

        return StatusCode.INTERNAL_SERVER_ERROR

    @staticmethod
    def updatePokemonByID(pokemonID: str, pokemonData: UserObj):
        print(f"pokemonID: {pokemonID}")
        print(f"isPokemonID a string: {isinstance(pokemonID, str)}")
        print(f"pokemonData: {pokemonData}\n")

        HandlerImage.saveImg(pokemonData)

        extensionImage = pathlib.Path(pokemonData.image).suffix
        urlImage = "/" + pokemonData.id +  extensionImage

        pokemonData.image = urlImage
        try:
            HandlerImage.addLinkImage(urlImage, extensionImage)
        except:
            print("erro in link image")
        database: dict = HandlerDatabase.getData()

        if database is None:
            return StatusCode.INTERNAL_SERVER_ERROR
        status = StatusCode.OK
        isPokemonRegistered, pokemonIndex = HandlerDatabase.isPokemonRegistered(pokemonID)
        if isPokemonRegistered:
            arePokemonEqual = HandlerDatabase.arePokemonsEqual(
                    database["users"][pokemonIndex][pokemonID],
                    pokemonData.__dict__())

            if not arePokemonEqual:
                database["users"][pokemonIndex][pokemonID] = pokemonData.__dict__()
            else:
                print("NOT MODIFIED")
                status = StatusCode.NOT_MODIFIED
        else:
            status = StatusCode.NOT_FOUND

        if HandlerDatabase.setData(database):
            return status

        return StatusCode.INTERNAL_SERVER_ERROR

    @staticmethod
    def deletePokemonByID(pokemonID: str):
        database = HandlerDatabase.getData()

        if database is None:
            return StatusCode.INTERNAL_SERVER_ERROR

        status = StatusCode.OK

        isPokemonRegistered, pokemonIndex = HandlerDatabase.isPokemonRegistered(pokemonID)
        imageLink = ''
        if isPokemonRegistered:
            imageLink = database["users"][pokemonIndex][pokemonID]['image']
            database["users"].pop(pokemonIndex)
            HandlerImage.deleteImg(pokemonID, imageLink)
        else:
            status = StatusCode.NOT_FOUND

        if HandlerDatabase.setData(database):
            return status
        

        return StatusCode.INTERNAL_SERVER_ERROR

    @staticmethod
    def deleteAllPokemons():
        database = HandlerDatabase.getData()

        if database is None:
            return StatusCode.INTERNAL_SERVER_ERROR

        database["users"] = []

        if HandlerDatabase.setData(database):
            return StatusCode.OK

        return StatusCode.INTERNAL_SERVER_ERROR

    @staticmethod
    def isPokemonRegistered(pokemonID: str):
        database = HandlerDatabase.getData()

        if database is None:
            return False, None

        index: int
        element: dict
        for index, element in enumerate(database["users"]):
            if pokemonID == list(element.keys())[0]:
                return True, index

        return False, None

    @staticmethod
    def getSizeList():
        database = HandlerDatabase.getData()

        if database is None:
            return -1

        return len(database["users"])

    @staticmethod
    def getData():
        try:
            with open(HandlerDatabase.pokemonDatabasePath, 'r+') as file:
                HandlerDatabase.pokemonDatabase = json.load(file)
                return HandlerDatabase.pokemonDatabase
        except:
            return None

    @staticmethod
    def setData(data: dict):
        HandlerDatabase.pokemonDatabase = data
        try:
            with open(HandlerDatabase.pokemonDatabasePath, 'w+') as file:
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

                return True
        except:
            print(f"HandlerDatabase::setData() exception")
            return False

    @staticmethod
    def arePokemonsEqual(pokemonA: dict, pokemonB: dict):
        print(pokemonA)
        print(pokemonB)
        for k, v in pokemonA.items():
            if v != pokemonB[k]:
                return False
        return True
