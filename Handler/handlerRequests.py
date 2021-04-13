from server import *
from threading import Thread

class Handler(Thread):
    def __init__ (self, server):
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
                   print(request)
                   
                   break
                   
            print("close connection...")
            connectionSocket.close()
            