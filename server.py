from socket import *
from handler.HandlerRequests import Handler


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSocket.bind((self.ip, self.port))
        serverSocket.listen(1)    
        self.serverSocket = serverSocket

        self.handler = Handler(self)
        self.handler.start()     


def startServer():
    serverHttp = Server('localhost', 8080)
    print("Server started on " + serverHttp.ip + ":" + str(serverHttp.port))
