from server import *
from threading import Thread
from Message.request import Request

class HandlerErrors():

    @staticmethod
    def sendErrorCode(msg, connectionSocket):
       print("Deu Erro")
       connectionSocket.send(("HTTP/1.1 400 BAD REQUEST\n").encode())
       connectionSocket.close()
