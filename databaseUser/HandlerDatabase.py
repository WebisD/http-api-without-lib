from message.StatusCode import StatusCode
import json
from databaseUser.ObjectUser import UserObj
from handler.HandlerImage import HandlerImage


class HandlerDatabase:
    pokemonDatabasePath: str = 'databaseUser/database.json'
    pokemonDatabase: dict = {}

    @staticmethod
    def insertPokemon(obj: UserObj) -> StatusCode:
        """ Insert a new object in the database

        :param obj: Object to be inserted
        :returns: Status code of this insertion

        """
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
    def updatePokemonByID(pokemonID: str, pokemonData: UserObj) -> StatusCode:
        """ Update an object present in the database

        :param pokemonID: Object ID to be updated
        :param pokemonData: New object information
        :returns: Status code of this update

        """
        print(f"Update pokemonID: {pokemonID}")

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
    def deletePokemonByID(pokemonID: str) -> StatusCode:
        """ Delete an object present in the database

        :param pokemonID: Object ID to be deleted
        :returns: Status code of this operation

        """
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
    def deleteAllPokemons() -> StatusCode:
        """ Delete all objects in the database
        
        :returns: Status code of this operation

        """
        database = HandlerDatabase.getData()

        if database is None:
            return StatusCode.INTERNAL_SERVER_ERROR

        database["users"] = []

        if HandlerDatabase.setData(database) and HandlerImage.delete_all_images():
            return StatusCode.OK

        return StatusCode.INTERNAL_SERVER_ERROR

    @staticmethod
    def isPokemonRegistered(pokemonID: str) -> (bool, int):
        """ Check if object exists in database
        
        :param pokemonID: Object ID to be checked
        :returns: If the object exists and the index in the database

        """
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
    def getSizeList() -> int:
        """ Get number of objects in database
        
        :returns: Size of object list

        """
        database = HandlerDatabase.getData()

        if database is None:
            return -1

        return len(database["users"])

    @staticmethod
    def getData() -> any:
        """ Read json file and set dictionary with values
        
        :returns: Dictionary with the list of objects or None

        """
        try:
            with open(HandlerDatabase.pokemonDatabasePath, 'r+') as file:
                HandlerDatabase.pokemonDatabase = json.load(file)
                return HandlerDatabase.pokemonDatabase
        except:
            return None

    @staticmethod
    def setData(data: dict) -> bool:
        """ Write json file with dictionary

        :param data: dictionary containing the database
        :returns: If can be updated or not

        """
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
    def arePokemonsEqual(pokemonA: dict, pokemonB: dict) -> bool:
        """ Compare two dicionaries
        
        :returns: If the dictionaries are equal or not

        """
        for k, v in pokemonA.items():
            if k != 'image' and v != 'image':
                if  v != pokemonB[k]:
                    return False
        return True

    @staticmethod
    def areImagesEqual(current_image, new_image) ->(bool, str):
        """ Compare two images
        
        :returns: If the images are equal or not and the dataURI of image

        """
        current_data = HandlerImage.image_to_data(current_image)

        if current_data == new_image or new_image.find("http://localhost:") != -1:
            return True, None

        return False, new_image
