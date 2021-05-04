from threading import Thread

from message.ParserMessage import ParserMessage
from message.Request import Request
from message.StatusCode import StatusCode

from handler.HandlerErrors import HandlerErrors
from methods.DELETE import DELETE
from methods.GET import GET
from methods.POST import POST
from methods.PUT import PUT

import time


def recv(sock, chunkSize=8192, timeout=2):
    fragments = []

    data = None

    while True:
        data = sock.recv(chunkSize)
        print(data, end="\n\n\n\n\n\n\n")

        if not data:
            return b"".join(fragments)

        fragments.append(data)


class Handler(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

    def run(self):
        while True:
            connectionSocket, addr = self.server.serverSocket.accept()
            
            while True:
                request = recv(connectionSocket, 8192).decode()
                # request = connectionSocket.recv(100000).decode()
                print(request)
        
                if not request: 
                    break

                request = Request(ParserMessage.parseRequest(request))
                request.setIp(addr)

                # self.checkTypeRequest(request, connectionSocket)
                response = self.getResponseToRequest(request)
                connectionSocket.send(response)
                break

    def getResponseToRequest(self, request):
        response: str

        if request.type == "GET":
            response = GET.response(request)
        elif request.type == "POST":
            response = POST.response(request)
        elif request.type == "PUT":
            response = PUT.response(request)
        elif request.type == "DELETE":
            response = DELETE.response(request)
        else:
            response = HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)

        return response

    # def checkTypeRequest(self, request, connectionSocket):
    #     response = {}
    #
    #     try:
    #         response = eval(request.type).response(request)
    #     except Exception as e:
    #         print(e)
    #         response = HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)
    #     connectionSocket.send(response)
    #     connectionSocket.close()
