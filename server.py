from socket import *
from threading import Thread
import sys
from Handler.handlerRequests import Handler
from Methods.GET import GET
from Methods.POST import POST
from Methods.PUT import PUT
from Methods.DELETE import DELETE

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind((self.ip, self.port))
        serverSocket.listen(1)    
        self.serverSocket = serverSocket

        self.handler = Handler(self)
        self.handler.start()     

def startServer():
    serverHttp = Server('localhost', 8080)
    print("Server started on " + serverHttp.ip + ":" + str(serverHttp.port))
