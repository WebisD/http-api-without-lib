from Message.request import Request
from DatabaseUser.handlerDatabase import HandlerDatabase
import json

class PUT():

    @staticmethod
    def response(request):
        data = json.loads(request.body)

        print(data)
        return "aaaa".encode()
