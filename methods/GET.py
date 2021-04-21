from message.Request import Request
from message.Response import Response
from message.StatusCode import StatusCode
import os
from datetime import datetime

class GET:
    urlTable = {
        "/": {"type": "text/html", "filePath": "./assets/index.html"},
        "/bootstrap.min.css": {"type": "text/css", "filePath": "./assets/bootstrap.min.css"},
        "/dashboard.css": {"type": "text/css", "filePath": "./assets/dashboard.css"},
        "/bootstrap-4.0.0/assets/js/vendor/popper.min.js": {"type": "text/css", "filePath": "./assets/bootstrap-4.0.0/assets/js/vendor/popper.min.js"},
        "/bootstrap-4.0.0/dist/js/bootstrap.min.js": {"type": "text/css", "filePath": "./assets/bootstrap-4.0.0/dist/js/bootstrap.min.js"},
        "/favicon.ico": {"type": "image/*", "filePath": "./assets/bootstrap-4.0.0/favicon.ico"},
        "/favicon.svg": {"type": "image/*", "filePath": "./assets/bootstrap-4.0.0/favicon.svg"},
        "/error": {"type": "text/html", "filePath": "./assets/error.html"},
        "/datatabase": {"type": "application/json", "filePath": "./databaseUser/database.json"},
    }

    @staticmethod
    def response(request: Request):
        url = request.URI if request.URI in GET.urlTable else "/error"
        response: Response = Response(status_code=StatusCode.BAD_REQUEST, body="", header={})

        with open(GET.urlTable[url]["filePath"], 'r', encoding='utf-8', errors='replace') as file:
            response.status_code = StatusCode.OK.value
            response.body = "".join(file.readlines())
            contentLength = os.stat(file.name).st_size
            lastModified = datetime.fromtimestamp(os.stat(file.name).st_mtime).strftime("%d %b %Y %H:%M:%S GMT")

        response.headers["Content-Length"] = contentLength
        response.headers["Last-Modified"] = lastModified
        response.headers["Content-Type"] = GET.urlTable[url]["type"]
        response.headers["Connection"] = "Closed"

        print(response.body)

        return response.encodeResponse()

