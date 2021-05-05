from threading import Thread

from message.ParserMessage import ParserMessage
from message.Request import Request
from message.StatusCode import StatusCode

from handler.HandlerErrors import HandlerErrors
from methods.DELETE import DELETE
from methods.GET import GET
from methods.POST import POST
from methods.PUT import PUT
import string


def recv(sock, chunkSize=8192):
    fragments = []

    data = None

    while True:
        print("Entrei no rcv")
        data = sock.recv(chunkSize)

        if data is None:
            print("Data vazia")
            return

        try:
            decoded_data = data.decode()
            if decoded_data.find("GET /") != -1 or decoded_data.find("PUT /") != -1 or decoded_data.find(
                    "DELETE /") != -1:
                # Not a post, return
                print("NAP: ")
                print(data)
                return data

            print("É um POST")
            #print(50 * '-')
            print(data)
            #print(50 * '-')

            #if decoded_data[0] == '{' and decoded_data[-1] != '}':
            #    fragments.append(data[:-1])
            #else:
            fragments.append(data)
            if decoded_data[-1] == '}':
                print("vou sair")

                a = b"".join(fragments)

                print("rcv() retornou:")
                print(a)
                return a

        except Exception as e:
            print(e)


class Handler(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

    def run(self):
        while True:
            print("No aguardo")
            connectionSocket, addr = self.server.serverSocket.accept()

            while True:
                request = recv(connectionSocket, 8192).decode()
                # request = connectionSocket.recv(8192).decode()

                print("Sai do recv()")
                ##print(request)

                if not request:
                    print("SAI")
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
