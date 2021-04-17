from Methods.method import Method
from Message.request import Request

class Put():
    @staticmethod
    def response(msg, connectionSocket):
        statusOperation = HandlerObj.put(msg)
        print(requestBody)
