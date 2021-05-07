class Request:
    """Responsible for encapsulating a parsed request"""

    def __init__(self, request_message: dict) -> None:
        """Initializes the Request class instance's attributes

        :param request_message: A dictionary containing a parsed request
        :returns: None

        """
        self.type: str = request_message['Request-Type']
        self.URI: str = request_message['Request-URI']
        self.http_version: str = request_message['HTTP-Version']
        self.host: str = request_message['Host']
        self.connection: str = request_message['Connection']
        self.user_agent: str = request_message['User-Agent']
        self.body: str = request_message['body']
        self.valid_content: str = None if 'Accept' not in request_message else request_message['Accept']
        self.accept_encoding: str = request_message['Accept-Encoding']
        self.accept_language: str = None if 'Accept-Language' not in request_message else request_message['Accept-Language']
        self.cookie: str = None if 'Cookie' not in request_message else request_message['Cookie']
        self.content_type: str = None if 'Content-Type' not in request_message else request_message['Content-Type']
        self.cache: str = None if 'Cache-Control' not in request_message else request_message['Cache-Control']
        self.content_length: str = None if 'Content-Length' not in request_message else request_message['Content-Length']

        self.ip = ""

    def setIp(self, ip: str) -> None:
        """Responsible for setting a new value to the ip attribute of the Request class instance

        :param ip: A string containing the new ip
        :returns: None

        """
        self.ip = ip

    def __str__(self) -> str:
        """Returns a string representation of the Request class instance"""
        return f'{self.type, self.URI, self.http_version, self.host, self.body}...'
