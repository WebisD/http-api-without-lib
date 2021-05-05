from message.StatusCode import StatusCode
import json
from databaseUser.ObjectUser import UserObj


class HandlerDatabase:
    pokemonDatabasePath: str = 'databaseUser/database.json'
    pokemonDatabase: dict = {}

    @staticmethod
    def insertPokemon(obj: UserObj):
        """ Executa uma inserção de um novo objeto no database

        :param obj: Objeto a ser inserido
        :returns: O status code dessa inserção

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
    def updatePokemonByID(pokemonID: str, pokemonData: UserObj):
        """ Executa uma atualização de um objeto existente no database
        
        :param pokemonID: ID do objeto a ser atualizado
        :param pokemonData: Informações atualizadas do objeto
        :returns: O status code dessa atualização

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
    def deletePokemonByID(pokemonID: str):
        """ Executa uma remoção de um objeto existente no database
        
        :param pokemonID: ID do objeto a ser deletado
        :returns: O status code dessa remoção

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
    def deleteAllPokemons():
        """ Executa uma remoção de todos os objetos existentes no database
        
        :returns: O status code dessa remoção

        """
        database = HandlerDatabase.getData()

        if database is None:
            return StatusCode.INTERNAL_SERVER_ERROR

        database["users"] = []

        if HandlerDatabase.setData(database):
            return StatusCode.OK

        return StatusCode.INTERNAL_SERVER_ERROR

    @staticmethod
    def isPokemonRegistered(pokemonID: str):
        """ Executa uma checagem de ID, para conferir se o objeto existe no database
        
        :param pokemonID: ID do objeto a ser checado
        :returns: Se o objeto está registrado e o índice no database (caso exista)

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
    def getSizeList():
        """ Executa uma leitura do database para ver o tamanho da lista
        
        :returns: O tamanho da lista de objetos presentes no database

        """
        database = HandlerDatabase.getData()

        if database is None:
            return -1

        return len(database["users"])

    @staticmethod
    def getData():
        """ Executa uma leitura do arquivo database JSON
        
        :returns: A lista de objetos presentes no arquivo JSON

        """
        try:
            with open(HandlerDatabase.pokemonDatabasePath, 'r+') as file:
                HandlerDatabase.pokemonDatabase = json.load(file)
                return HandlerDatabase.pokemonDatabase
        except:
            return None

    @staticmethod
    def setData(data: dict):
        """ Executa uma atualização do JSON

        :param data: dicionário contendo o database
        :returns: Se conseguiu atualizar o arquivo JSON ou não

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
    def arePokemonsEqual(pokemonA: dict, pokemonB: dict):
        """ Executa uma comparação entre dois dicionários, referentes a dois objetos
        
        :returns: Se os dicionários são iguais ou não

        """
        for k, v in pokemonA.items():
            if v != pokemonB[k]:
                return False
        return True
