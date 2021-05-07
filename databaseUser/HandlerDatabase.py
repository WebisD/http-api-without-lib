from message.StatusCode import StatusCode
import json
from databaseUser.ObjectUser import UserObj
from handler.HandlerImage import HandlerImage


class HandlerDatabase:
    pokemonDatabasePath: str = 'databaseUser/database.json'
    pokemonDatabase: dict = {}

    @staticmethod
    def insertPokemon(obj: UserObj):
        database: dict = HandlerDatabase.getData()

        if database is None:
            return StatusCode.INTERNAL_SERVER_ERROR

        image_path = HandlerImage.insert_image_database(obj.image, obj.id)

        if image_path is None:
            return StatusCode.INTERNAL_SERVER_ERROR

        pokemonID = obj.id
        pokemonData = {
            "name": obj.name,
            "phone": obj.phone,
            "pokemon": obj.pokemon,
            "image": image_path
        }

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
        print(f"Update pokemonID: {pokemonID}")
        print(f"pokemonData: {pokemonData}\n")

        database: dict = HandlerDatabase.getData()

        if database is None:
            return StatusCode.INTERNAL_SERVER_ERROR

        status = StatusCode.OK

        isPokemonRegistered, pokemonIndex = HandlerDatabase.isPokemonRegistered(pokemonID)
        if isPokemonRegistered:
            current = database["users"][pokemonIndex][pokemonID]
            new = pokemonData.__dict__()

            arePokemonEqual = HandlerDatabase.arePokemonsEqual(current, new)
            areImageEqual, data_URI = HandlerDatabase.areImagesEqual(current["image"], new["image"])

            if not areImageEqual:
                new["image"] = HandlerImage.insert_image_database(data_URI, pokemonID)

            if not arePokemonEqual:
                database["users"][pokemonIndex][pokemonID] = new
            else:
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
        if isPokemonRegistered:
            image = database["users"][pokemonIndex][pokemonID]["image"]
            deleted_image = HandlerImage.delete_image_database(image)
            database["users"].pop(pokemonIndex)
            if not deleted_image:
                status = StatusCode.OK
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

        if HandlerDatabase.setData(database) and HandlerImage.delete_all_images():
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

        for k, v in pokemonA.items():
            if k != 'image' and v != 'image':
                if  v != pokemonB[k]:
                    return False
        return True

    @staticmethod
    def areImagesEqual(current_image, new_image):
        current_data = HandlerImage.image_to_data(current_image)

        if current_data == new_image or new_image.find("http://localhost:") != -1:
            return True, None

        return False, new_image
