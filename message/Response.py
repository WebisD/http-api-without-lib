import enum
from datetime import datetime
from message.StatusCode import StatusCode


class Response:
    """Responsible for encapsulating the response headers and body"""

    def __init__(self, status_code: enum.Enum, body: str, header: dict) -> None:
        """Initializes the Response class instance's attributes

        :param status_code: A StatusCode enum object representing the outcome of the request
        :param body: A string containing the content of the response
        :param header: A dictionary containing the headers of the response
        :returns: None

        """
        self.protocol: str = "HTTP/1.1"
        self.status_code: StatusCode.StatusCode = status_code
        self.body: str = body
        self.headers: dict = header
        self.server: str = "Apache/2.22.14 (Ubuntu-20.04)"

    def encodeResponse(self) -> bytes:
        """Responsible for encoding the string representation of the Response class instance

        returns: A byte object containing the Response class instance

        """

        response = self.__str__()

        return response.encode()

    """TODO: put the image bytes object as an argument instead of storing it in the body to keep consistency across 
    our code """
    def encodeResponseImages(self) -> bytes:
        """Responsible for encoding the response along with the image

        returns: A byte object containing the response headers and body along with the image

        """

        response = ""
        response += self.statusLine() + "\n"
        response += self.headerLine()
        response += self.server + "\n"
        response += "\n"

        return response.encode() + self.body

    def statusLine(self):
        """Responsible for creating a string with the protocol and status

        :returns: A string containing the protocol and the status

        """
        return f'{self.protocol} {self.status_code.value[0]} {self.status_code.value[1]}'

    def headerLine(self) -> str:
        """Responsible for creating a string containing the headers information

        :returns: A string containing the headers information

        """
        header = ""
        header += Response.getDate() + "\n"

        for key in self.headers:
            header += f'{key}: {self.headers[key]}'
            header += '\n'

        return header

    @staticmethod
    def getDate() -> str:
        """Responsible for creating a string with the current date

        :returns: A string containing the current date

        """

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        time = datetime.now()

        current_day = days[time.weekday()]

        date = time.strftime("%d %b %Y %H:%M:%S GMT")

        return f'{current_day}, {date}'

    @staticmethod
    def getDateFromSeconds(seconds: float) -> str:
        """Creates a date from the given seconds

        :param seconds: A float number containing the total date in seconds
        :returns: A string containing the date created from the given second

        """

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        time = datetime.fromtimestamp(seconds)
        current_day = days[time.weekday()]

        date = time.strftime("%d %b %Y %H:%M:%S GMT")

        return f'{current_day}, {date}'

    def __str__(self) -> str:
        """Responsible for representing the class as a string

        :returns: A string representation of the Response class instance

        """

        response = ""
        response += self.statusLine() + "\n"
        response += self.headerLine()
        response += self.server + "\n"
        response += "\n"
        response += self.body

        return response
