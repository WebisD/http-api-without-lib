from datetime import datetime


class Response:
    def __init__(self, status_code, last_modified, body, header):
        self.protocol = "HTTP/1.1"
        self.status_code = status_code
        self.last_modified = last_modified
        self.body = body
        self.headers = header
        self.status_code = status_code.value
        self.time = datetime.now()

    def sendResponse(self):
        response = ""
        response += self.statusLine()
        response += self.headerLine()
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
        header += self.getDate()
        header += self.last_modified + '\n'

        for key in self.headers:
            header += f'{key}: {self.headers[key]}'
            header += '\n'

        return header

    def getDate(self):
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        current_day = days[self.time.weekday()]

        date = self.time.strftime("%d %b %Y %H:%M:%S GMT")

        return f'{current_day}, {date}'
