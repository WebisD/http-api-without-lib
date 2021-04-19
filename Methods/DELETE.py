from Message.request import Request

class DELETE():
    arrayUrl = {}

    @staticmethod
    def response(request):
        arrayUrl[request.uri]()


