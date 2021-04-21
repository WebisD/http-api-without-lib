class Request:
    def __init__(self, request_message):
        self.type = request_message['Request-Type']
        self.URI = request_message['Request-URI']
        self.http_version = request_message['HTTP-Version']
        self.host = request_message['Host']
        self.connection = request_message['Connection']
        self.user_agent = request_message['User-Agent']
        self.body = request_message['body']
        self.valid_content = None if 'Accept' not in request_message else request_message['Accept']
        self.accept_encoding = request_message['Accept-Encoding']
        self.accept_language = None if 'Accept-Language' not in request_message else request_message['Accept-Language']
        self.cookie = None if 'Cookie' not in request_message else request_message['Cookie']
        self.content_type = None if 'Content-Type' not in request_message else request_message['Content-Type']
        self.cache = None if 'Cache-Control' not in request_message else request_message['Cache-Control']
        self.content_length = None if 'Content-Length' not in request_message else request_message['Content-Length']

        self.ip = ""

    def setIp(self, ip):
        self.ip = ip

    def __str__(self):
        return f'{self.type, self.URI, self.http_version, self.host, self.body}...'
