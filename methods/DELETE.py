from databaseUser.HandlerDatabase import HandlerDatabase
from handler.HandlerErrors import HandlerErrors
from message.Response import Response
from message.StatusCode import StatusCode

class DELETE:
    @staticmethod
    def response(request):
        if request.URI != "/":
            idUrl = DELETE.getIdOfUrl(request.URI)
            lastId = HandlerDatabase.getSizeList()

            if 0 <= idUrl <= lastId:
                status = HandlerDatabase.deleteObj(idUrl)
                body = '<html><head></head><body><h1>Hello World<h1></body></html>'
                header = {
                    "Content-Length": "88",
                    "Content-Type": "text/html",
                    "Connection": "Closed",
                    "Last-Modified": "Wed, 22 Jul 2009 19:15:56 GMT"
                }
                response = Response(status_code=status, body=body, header=header)

                return response.encodeResponse()
        else:
            status = HandlerDatabase.deleteAllObj()
            body = '<html><head></head><body><h1>Hello World<h1></body></html>'
            header = {
                "Content-Length": "88",
                "Content-Type": "text/html",
                "Connection": "Closed",
                "Last-Modified": "Wed, 22 Jul 2009 19:15:56 GMT"
            }
            response = Response(status_code=status, body=body, header=header)
            return response.encodeResponse()

        return HandlerErrors.sendErrorCode(request, StatusCode.BAD_REQUEST)

    @staticmethod
    def getIdOfUrl(URI):
        if len(URI) > 5 and URI.rfind("/?id=") != -1:
            return int(URI[5: len(URI)])
        return -1
