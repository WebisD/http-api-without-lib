import datetime


class UserObj:
    def __init__(self, name: str, phone: str, pokemon: str, image: str) -> None:
        """ Create an object of type UserObj, besides that
        will be create an ID based on the date of the creation time
    
        :param name: Contact name
        :param phone: Contact phone
        :param pokemon: Contact's favorite Pokémon
        :param image: Contact DataURL

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

    def setId(self, newID) -> None:
        """ Set the object ID
    
        :param newID: New object ID

        """
        self.id = newID

    def __hash__(self) -> str:
        """ Get the UserObj hash

        :returns: Object hash

        """
        return hash((
            self.name,
            self.phone,
            self.pokemon,
            self.image,
            datetime.datetime.now().strftime("%d %b %Y %H:%M:%S GMT")
        ))

    def __dict__(self) -> dict:
        """ Make a cast from UserObj to dictionary
        
        :returns: A dictionary based on the UserObj object

        """
        return {
            "name": self.name,
            "phone": self.phone,
            "pokemon": self.pokemon,
            "image": self.image
        }

    def __str__(self) -> str:
        """ Add the object's parameters in a String
        
        :returns: A String containing the object's attributes

        """
        return f"{{'{self.id}': {{" \
               f"name: '{self.name}'," \
               f" phone: '{self.phone}'," \
               f" pokemon: '{self.pokemon}'," \
               f" image: '{self.image}' " \
               f"}} " \
               f"}}"

    @staticmethod
    def fromDict(data: dict) -> UserObj:
        """ Make a cast from dictionary to UserObj 
 
        :returns: The dictionary based on UserObj object

        """
        return UserObj(data['name'], data['phone'], data['pokemon'], data['image'])
