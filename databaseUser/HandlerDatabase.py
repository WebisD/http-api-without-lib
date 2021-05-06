from message.StatusCode import StatusCode
import json
from databaseUser.ObjectUser import UserObj


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

        pokemonID = obj.id
        pokemonData = {
            "name": obj.name,
            "phone": obj.phone,
            "pokemon": obj.pokemon,
            "image": obj.image
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
        print(f"pokemonID: {pokemonID}")
        print(f"isPokemonID a string: {isinstance(pokemonID, str)}")
        print(f"pokemonData: {pokemonData}\n")

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
            database["users"].pop(pokemonIndex)
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

        if HandlerDatabase.setData(database):
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
    def getData() -> dict:
        """ Read json file and set dictionary with values
        
        :returns: Dictionary with the list of objects

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
        print(data)
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
            if v != pokemonB[k]:
                return False
        return True
