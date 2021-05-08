import socket

from threading import Thread

from message.ParserMessage import ParserMessage
from message.Request import Request
from message.StatusCode import StatusCode

from methods.GET import GET
from methods.POST import POST
from methods.PUT import PUT
from methods.DELETE import DELETE

from handler.HandlerErrors import HandlerErrors


def recv(sock: socket.socket, chunkSize: int = 8192) -> any:
    """Responsible for receiving all the request message chunks from the socket

    :param sock: the tcp socket responsible for receiving and sending messages
    :param chunkSize: the size of each incoming request message fragment
    :returns: A byte object containing the whole request message or None

    """

    fragments = []

    data = None

    while True:
        data = sock.recv(chunkSize)

        if data is None:
            return

        try:
            decoded_data = data.decode()
            if decoded_data.find("GET /") != -1 or decoded_data.find("DELETE /") != -1:
                # Not a post, return
                return data

            fragments.append(data)
            if decoded_data[-1] == '}':

                a = b"".join(fragments)
                return a

        except Exception as e:
            print(e)


class Handler(Thread):
    """Class responsible for handling incoming requests and sending responses"""

    def __init__(self, server) -> None:
        """Initializes the class instances attributes

        :param server: A server object containing the socket, host ip and host port
        :returns: None

        """

        Thread.__init__(self)
        self.server = server

    def run(self) -> None:
        """Responsible for running the server

        :returns: None

        """

        while True:
            connectionSocket, addr = self.server.serverSocket.accept()
            
            while True:
                request = recv(connectionSocket, 8192).decode()
        
                if not request: 
                    break
                else:
                    request = Request(ParserMessage.parseRequest(request))
                    request.setIp(addr)
                    
                    self.checkTypeRequest(request, connectionSocket)
                    break

    def checkTypeRequest(self, request: Request, connectionSocket: socket.socket) -> None:
        """Responsible for checking the request type and calling the appropriate method

        :param request: A Request object
        :param connectionSocket: A tcp socket
        :returns: None

        """
        response = {}
        
        try:
            response = eval(request.type).response(request)
        except Exception as e:
            print(e)
            response = HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)
        connectionSocket.send(response)
        connectionSocket.close()
