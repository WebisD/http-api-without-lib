from message.Request import Request
from message.Response import Response
from message.StatusCode import StatusCode
import os
from datetime import datetime
from handler.HandlerErrors import HandlerErrors


class GET:
    urlTable = {
        "/": {"type": "text/html", "filePath": "./assets/index.html"},
        "/bootstrap.min.css": {"type": "text/css", "filePath": "./assets/bootstrap.min.css"},
        "/dashboard.css": {"type": "text/css", "filePath": "./assets/dashboard.css"},
        "/popper.min.js": {"type": "text/css", "filePath": "./assets/bootstrap-4.0.0/assets/js/vendor/popper.min.js"},
        "/bootstrap.min.js": {"type": "text/css", "filePath": "./assets/bootstrap-4.0.0/dist/js/bootstrap.min.js"},
        "/datatabase": {"type": "application/json", "filePath": "./databaseUser/database.json"},
    }

    @staticmethod
    def response(request: Request):
        if request.URI in GET.urlTable:
            response: Response = Response(status_code=StatusCode.OK, body="", header={})

            with open(GET.urlTable[request.URI]["filePath"], 'r', encoding='utf-8', errors='replace') as file:
                response.status_code = StatusCode.OK
                response.body = "".join(file.readlines())
                contentLength = os.stat(file.name).st_size
                lastModified = datetime.fromtimestamp(os.stat(file.name).st_mtime).strftime("%d %b %Y %H:%M:%S GMT")

                response.headers["Last-Modified"] = lastModified
                # response.headers["Content-Length"] = contentLength
                response.headers["Content-Type"] = GET.urlTable[request.URI]["type"]
                response.headers["Connection"] = "Closed"

            return response.encodeResponse()

        return HandlerErrors.sendErrorCode(request, StatusCode.NOT_FOUND)
