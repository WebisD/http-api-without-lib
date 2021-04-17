from server import *
from threading import Thread

from Message.parserMessage import ParserMessage
from Message.request import Request
from Methods.GET import Get
from Methods.POST import Post
from Methods.PUT import Put
from Methods.DELETE import Delete

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
                    msg = Request(ParserMessage.parse(request))
                    msg.setIp(addr)
                    
                    self.checkTypeRequest(msg, connectionSocket)
                    break

    def checkTypeRequest(self, msg, connectionSocket):
        if msg.type == 'GET':
            Get.response(msg, connectionSocket)
        elif msg.type == 'POST':
            Post.response(msg, connectionSocket)
        elif msg.type == 'PUT':
            Put.response(msg, connectionSocket)
        elif msg.type == 'DELETE':
            Delete.response(msg, connectionSocket)
        else:
            HandlerErrors.sendErrorCode(msg, connectionSocket)
