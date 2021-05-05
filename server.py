from socket import *
from handler.HandlerRequests import Handler


class Server:
    def __init__(self, ip, port):
        """ Realiza a criação de um objeto do tipo Server, além disso
        irá criar um handler que eexecutará em uma thread esperando as requisições
    
        :param ip: IP onde o servidor ficará alocado
        :param port: Porta onde o servidor ficará alocado

        """
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
    """ Realiza a intanciação de um objeto do tipo Server, alocando-o no 
    ip local e na porta 8080
        
    """
    serverHttp = Server('localhost', 8083)
    print("Server started on " + serverHttp.ip + ":" + str(serverHttp.port))
