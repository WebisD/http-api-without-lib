from server import *
from threading import Thread

from Message.parserMessage import ParserMessage
from Message.request import Request
from Methods.GET import GET
from Methods.POST import POST
from Methods.PUT import PUT
from Methods.DELETE import DELETE

from Handler.handlerErrors import HandlerErrors

class Handler(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

    def run(self):
        while True:
            connectionSocket, addr = self.server.serverSocket.accept()
            
            while True:
                request = connectionSocket.recv(1024).decode()
        
                if not request: 
                    break
                else:
                    request = Request(ParserMessage.parseRequest(request))
                    request.setIp(addr)
                    
                    self.checkTypeRequest(request, connectionSocket)
                    break

    def checkTypeRequest(self, request, connectionSocket):
        response = ""
        try:
            response = eval(request.type).response(request)
        except:
            response = HandlerErrors.sendErrorCode(request)

        response = (("HTTP/1.1 200 OK\n").encode())

        connectionSocket.send(response)
        connectionSocket.close()
