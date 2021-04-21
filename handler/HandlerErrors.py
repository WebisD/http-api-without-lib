from server import *
from threading import Thread
from message.Request import Request
from message import Response, StatusCode


class HandlerErrors:

    @staticmethod
    def sendErrorCode(request, statusCode):
        response: Response = Response.Response(status_code=statusCode, body="", header={})
        response.body = "<h1>" + response.status_code.value[1] + "</h1>"
        print(response)

        return response.encodeResponse()
