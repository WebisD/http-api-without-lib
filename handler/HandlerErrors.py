from server import *
from threading import Thread
from message.Request import Request
from message import Response, StatusCode


class HandlerErrors:
    urlTable = {
        "/error": {"type": "text/html", "filePath": "./assets/error.html"},
        "/bootstrap.min.css": {"type": "text/css", "filePath": "./assets/bootstrap.min.css"},
        "/dashboard.css": {"type": "text/css", "filePath": "./assets/dashboard.css"},
        "/popper.min.js": {"type": "text/css", "filePath": "./assets/popper.min.js"},
        "/bootstrap.min.js": {"type": "text/css", "filePath": "./assets/bootstrap.min.js"},
        "/favicon.ico": {"type": "image/x-icon", "filePath": "./assets/bootstrap-4.0.0/favicon.ico"},
    }

    @staticmethod
    def sendErrorCode(request, statusCode):
        response: Response = Response.Response(status_code=statusCode, body="", header={})

        error = HandlerErrors.urlTable['/error']
        path = error['filePath']

        page = open(path).read().format(status_code=statusCode.value[0], error_text=statusCode.value[1])


        response.body = page

        response.headers["Content-Length"] = len(response.body)
        response.headers["Content-Type"] = error["type"]
        response.headers["Connection"] = "Closed"

        return response.encodeResponse()
