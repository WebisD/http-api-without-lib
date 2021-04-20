from server import *
from threading import Thread
from message.Request import Request


class HandlerErrors:

    @staticmethod
    def sendErrorCode(msg):
        print("Deu Erro")
        return "HTTP/1.1 400 BAD REQUEST\n".encode()
