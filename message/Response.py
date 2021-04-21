from datetime import datetime


class Response:
    def __init__(self, status_code, body, header):
        self.protocol = "HTTP/1.1"
        self.status_code = status_code
        self.body = body
        self.headers = header
        self.status_code = status_code.value
        self.server = "Apache/2.22.14 (Ubuntu-20.04)"
        self.time = datetime.now()

    def encodeResponse(self):
        response = ""
        response += self.statusLine()
        response += self.headerLine()
        response += self.server
        response += '\n'
        response += self.body

        return response.encode()

    def statusLine(self):
        """
        :return: HTTP/1.1 200 OK
        """
        return f'{self.protocol} {self.status_code[0]} {self.status_code[1]}'

    def headerLine(self):
        """
        :return: Date: Mon, 27 Jul 2009 12:28:53 GMT
                 Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
                 Content-Length: 88
                 Content-Type: text/html
                 Connection: Closed
        """
        header = ""
        header += Response.getDate()

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
