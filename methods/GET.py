from message.Request import Request
from message.Response import Response
from message.StatusCode import StatusCode
import os
from handler.HandlerErrors import HandlerErrors
from databaseUser.HandlerDatabase import HandlerDatabase


class GET:
    urlTable = {
        "/": {"type": "text/html", "filePath": "./assets/index.html"},
        "/post": {"type": "text/html", "filePath": "./assets/post.html"},
        "/list": {"type": "text/html", "filePath": "./assets/list.html"},
        "/bootstrap.min.css": {"type": "text/css", "filePath": "./assets/bootstrap.min.css"},
        "/dashboard.css": {"type": "text/css", "filePath": "./assets/dashboard.css"},
        "/popper.min.js": {"type": "text/css", "filePath": "./assets/popper.min.js"},
        "/bootstrap.min.js": {"type": "text/css", "filePath": "./assets/bootstrap.min.js"},
        "/favicon.ico": {"type": "image/x-icon", "filePath": "./assets/bootstrap-4.0.0/favicon.ico"},
        "/database": {"type": "application/json", "filePath": "./databaseUser/database.json"},
        "/edit": {"type": "text/html", "filePath": "./assets/put.html"},
    }

    @staticmethod
    def response(request: Request):

        if request.URI.find('database') != -1 or request.URI.find('edit') != -1 or request.URI in GET.urlTable:
            response: Response = Response(status_code=StatusCode.OK, body="", header={})
            if request.URI.find('database') != -1:
                request.URI = '/database'
            if request.URI.find('edit') != -1:
                params = GET.getParamsFromURL(request.URI)
                if "id" in params.keys():
                    response.headers["pokemonID"] = params["id"]
                    request.URI = "/edit"
                else:
                    return HandlerErrors.sendErrorCode(request, StatusCode.NOT_FOUND)
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

    @staticmethod
    def getParamsFromURL(url):
        parsedParams: dict = {}
        elements = url.split('?')[1].split('&')
        for elem in elements:
            splitElem = elem.split('=')
            parsedParams[splitElem[0]] = splitElem[1]

        return parsedParams

