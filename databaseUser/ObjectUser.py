import datetime


class UserObj:
    def __init__(self, name: str, phone: str, pokemon: str, image: str):
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
        self.id = newID

    def __hash__(self):
        return hash((
            self.name,
            self.phone,
            self.pokemon,
            self.image,
            datetime.datetime.now().strftime("%d %b %Y %H:%M:%S GMT")
        ))

    def __dict__(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "pokemon": self.pokemon,
            "image": self.image
        }

    def __str__(self):
        return f"{{'{self.id}': {{" \
               f"name: '{self.name}'," \
               f" phone: '{self.phone}'," \
               f" pokemon: '{self.pokemon}'," \
               f" image: '{self.image}' " \
               f"}} " \
               f"}}"

    @staticmethod
    def fromDict(data: dict):
        return UserObj(data['name'], data['phone'], data['pokemon'], data['image'])
