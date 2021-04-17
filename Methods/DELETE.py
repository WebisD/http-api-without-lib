from Methods.method import Method
from Message.request import Request
from Handler.handlerObj import HandlerObj

class Delete():
    @staticmethod
    def response(msg, connectionSocket):
        statusOperation = HandlerObj.delete(msg)
        print(requestBody.http_version)
