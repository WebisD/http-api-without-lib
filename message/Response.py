from datetime import datetime
from message.StatusCode import StatusCode


class Response:
    """Responsible for encapsulating the response headers and body"""

    def __init__(self, status_code: StatusCode, body: str, header: dict) -> None:
        """Initializes the Response class instance's attributes

        :param status_code: A StatusCode object representing the outcome of the request
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
        """Responsible for encoding the string representation of the Response class instance"""

        response = self.__str__()

        return response.encode()

    """TODO: put the image bytes object as an argument instead of storing it in the body to keep consistency across 
    our code """
    def encodeResponseImages(self):
        """Responsible for encoding the response along with the image"""

        response = ""
        response += self.statusLine() + "\n"
        response += self.headerLine()
        response += self.server + "\n"
        response += "\n"

        return response.encode() + self.body

    def statusLine(self):
        """
        :returns: A string containing the protocol and the status
        """
        return f'{self.protocol} {self.status_code.value[0]} {self.status_code.value[1]}'

    def headerLine(self):
        """
        :returns: Date: Mon, 27 Jul 2009 12:28:53 GMT
                 Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
                 Content-Length: 88
                 Content-Type: text/html
                 Connection: Closed
        """
        header = ""
        header += Response.getDate() + "\n"

        for key in self.headers:
            header += f'{key}: {self.headers[key]}'
            header += '\n'

        return header

    @staticmethod
    def getDate():
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        time = datetime.now()

        current_day = days[time.weekday()]

        date = time.strftime("%d %b %Y %H:%M:%S GMT")

        return f'{current_day}, {date}'

    @staticmethod
    def getDateFromSeconds(seconds):
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        time = datetime.fromtimestamp(seconds)
        current_day = days[time.weekday()]

        date = time.strftime("%d %b %Y %H:%M:%S GMT")

        return f'{current_day}, {date}'

    def __str__(self):
        response = ""
        response += self.statusLine() + "\n"
        response += self.headerLine()
        response += self.server + "\n"
        response += "\n"
        response += self.body

        return response
