from abc import ABC, abstractmethod
from Message.message import Message

class Request(Message):
    def __init__(self, requestMessage):
        self.type = requestMessage['Request-Type']
        self.URI = requestMessage['Request-URI']
        self.http_version = requestMessage['HTTP-Version']
        self.host = requestMessage['Host']
        self.connection = requestMessage['Connection']
        self.user_agent = requestMessage['User-Agent']
        self.body = requestMessage['body']
        self.valid_content = requestMessage['Accept']
        self.accept_encoding = requestMessage['Accept-Encoding']
        self.accept_language = None if 'Accept-Language' not in requestMessage else requestMessage['Accept-Language']
        self.cookie = None if 'Cookie' not in requestMessage else requestMessage['Cookie']
        self.content_type = None if 'Content-Type' not in requestMessage else requestMessage['Content-Type']
        self.cache = None if 'Cache-Control' not in requestMessage else requestMessage['Cache-Control']
        self.content_length = None if 'Content-Length' not in requestMessage else requestMessage['Content-Length']

    def __str__(self):
        return f'{self.type, self.URI, self.http_version, self.host, self.body}...'

    def setIp(self, ip):
        self.ip = ip
