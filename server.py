from socket import *
from threading import Thread
import sys
from handlerRequests import Handler

class Server():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind((self.ip, self.port))
        serverSocket.listen(1)    
        self.serverSocket = serverSocket

        self.handler = Handler(self)
        self.handler.start()     

    def getMethod(self):
        print("get method")
    
    def putMethod(self):
        print("put method")

    def postMethod(self):
        print("post method")

    def deleteMethod(self):
        print("delete method")

def startServer():
    serverHttp = Server('localhost', 8080)
    print("Server started on " + serverHttp.ip + ":" + str(serverHttp.port))

#criar um objeto -> retornar como html