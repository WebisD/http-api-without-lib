from message.Request import Request
from message.Response import Response
from message.StatusCode import StatusCode
import os
from datetime import datetime
from handler.HandlerErrors import HandlerErrors


class GET:
    urlTable = {
        "/": {"type": "text/html", "filePath": "./assets/index.html"},
        "/post": {"type": "text/html", "filePath": "./assets/post.html"},
        "/list": {"type": "text/html", "filePath": "./assets/list.html"},
        "/database": {"type": "application/json", "filePath": "./databaseUser/database.json"},
        "/bootstrap.min.css": {"type": "text/css", "filePath": "./assets/bootstrap.min.css"},
        "/dashboard.css": {"type": "text/css", "filePath": "./assets/dashboard.css"},
        "/popper.min.js": {"type": "text/css", "filePath": "./assets/popper.min.js"},
        "/bootstrap.min.js": {"type": "text/css", "filePath": "./assets/bootstrap.min.js"},
        "/favicon.ico": {"type": "image/x-icon", "filePath": "./assets/bootstrap-4.0.0/favicon.ico"},
        "/database": {"type": "application/json", "filePath": "./databaseUser/database.json"},
    }

    @staticmethod
    def response(request: Request):

        if request.URI.find('database') != -1 or request.URI in GET.urlTable:
            response: Response = Response(status_code=StatusCode.OK, body="", header={})
            if request.URI.find('database') != -1 :
                request.URI = '/database'
            with open(GET.urlTable[request.URI]["filePath"], 'r', encoding='utf-8', errors='replace') as file:
                response.status_code = StatusCode.OK
                response.body = "".join(file.readlines())
                lastModified = Response.getDateFromSeconds(os.stat(file.name).st_mtime)

                response.headers["Last-Modified"] = lastModified
                response.headers["Content-Length"] = len(response.body)
                response.headers["Content-Type"] = GET.urlTable[request.URI]["type"]
                response.headers["Connection"] = "Closed"

            return response.encodeResponse()

        return HandlerErrors.sendErrorCode(request, StatusCode.NOT_FOUND)