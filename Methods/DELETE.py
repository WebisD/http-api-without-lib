from Message.request import Request
from Handler.handlerObj import HandlerObj

class Delete():
    @staticmethod
    def response(msg, connectionSocket):
        statusOperation = HandlerObj.delete(msg)
        connectionSocket.send(("HTTP/1.1 200 OK\n").encode())
        connectionSocket.close()
