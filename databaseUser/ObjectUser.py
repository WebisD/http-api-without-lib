import datetime


class UserObj:
    def __init__(self, name: str, phone: str, pokemon: str, image: str):
        """ Realiza a criação de um objeto do tipo UserObj, além disso
        irá criar um ID baseado na data do instante de criação
    
        :param name: Nome do contato
        :param phone: Telefone do contato
        :param pokemon: Pokemon favorito do contato
        :param image: DataURL do contato

        """
        self.name = name
        self.phone = phone
        self.pokemon = pokemon
        self.image = image
        self.id = ""
        self.setId(str(hash((
            self.name,
            self.phone,
            self.pokemon,
            self.image,
            datetime.datetime.now().strftime("%d %b %Y %H:%M:%S GMT")
        ))))

    def setId(self, newID):
        """ Defini o ID do objeto
    
        :param newID: Novo ID do objeto

        """
        self.id = newID

    def __hash__(self):
        """ Retornar o hash do UserObj 

        :returns: Hash do objeto

        """
        return hash((
            self.name,
            self.phone,
            self.pokemon,
            self.image,
            datetime.datetime.now().strftime("%d %b %Y %H:%M:%S GMT")
        ))

    def __dict__(self):
        """ Executa uma um cast de UserObj para dicionário
        
        :returns: Um dicionário baseado no objeto UserObj 

        """
        return {
            "name": self.name,
            "phone": self.phone,
            "pokemon": self.pokemon,
            "image": self.image
        }

    def __str__(self):
        """ Exibir os parametros do objeto numa String
        
        :returns: Uma String contendo os atributos do objeto

        """
        return f"{{'{self.id}': {{" \
               f"name: '{self.name}'," \
               f" phone: '{self.phone}'," \
               f" pokemon: '{self.pokemon}'," \
               f" image: '{self.image}' " \
               f"}} " \
               f"}}"

    @staticmethod
    def fromDict(data: dict):
        """ Executa uma um cast de dicionário para UserObj
        
        :returns: O objeto UserObj baseado no dicionário

        """
        return UserObj(data['name'], data['phone'], data['pokemon'], data['image'])
