from threading import Thread
from message.Request import Request
from message import Response, StatusCode
from string import Template


class HandlerErrors:
    """Class responsible for handling errors"""

    def __init__(self):
        pass

    urlTable = {
        "/error": {"type": "text/html", "filePath": "./assets/public/error.html"},
        "/bootstrap.min.css": {"type": "text/css", "filePath": "./assets/bootstrap.min.css"},
        "/dashboard.css": {"type": "text/css", "filePath": "./assets/dashboard.css"},
        "/popper.min.js": {"type": "text/css", "filePath": "./assets/popper.min.js"},
        "/bootstrap.min.js": {"type": "text/css", "filePath": "./assets/bootstrap.min.js"},
        "/logo.ico": {"type": "image/x-icon", "filePath": "./assets/bootstrap-4.0.0/favicon.ico"},
    }

    @staticmethod
    def sendErrorCode(request: any, statusCode: StatusCode) -> bytes:
        """Responsible for generating a page with the given status code

        :param request: An object representing the request data. DEPRECATED
        :param statusCode: A StatusCode object containing the the status soon to be shown in the page
        :returns: A byte object containing the response header and the error page in the body.

        """

        response: Response = Response.Response(status_code=statusCode, body="", header={})

        error = HandlerErrors.urlTable['/error']
        path = error['filePath']

        page = open(path).read()  # .format(status_code=statusCode.value[0], error_text=statusCode.value[1])
        ca = Template(page).safe_substitute({'status_code': statusCode.value[0], 'error_text': statusCode.value[1]})
        response.body = ca

        response.headers["Content-Length"] = len(response.body)
        response.headers["Content-Type"] = error["type"]
        response.headers["Connection"] = "Closed"

        return response.encodeResponse()
