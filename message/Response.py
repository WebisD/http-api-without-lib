from datetime import datetime
from message.StatusCode import StatusCode


class Response:
    def __init__(self, status_code, body, header):
        self.protocol: str = "HTTP/1.1"
        self.status_code: StatusCode.StatusCode = status_code
        self.body: str = body
        self.headers: dict = header
        self.server: str = "Apache/2.22.14 (Ubuntu-20.04)"

    def encodeResponse(self):
        response = self.__str__()

        return response.encode()

    def encodeResponseImages(self):
        response = ""
        response += self.statusLine() + "\n"
        response += self.headerLine()
        response += self.server + "\n"
        response += "\n"
        #esponse = response.encode()

        return response.encode() + self.body

    def statusLine(self):
        """
        :return: HTTP/1.1 200 OK
        """
        return f'{self.protocol} {self.status_code.value[0]} {self.status_code.value[1]}'

    def headerLine(self):
        """
        :return: Date: Mon, 27 Jul 2009 12:28:53 GMT
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
