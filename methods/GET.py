from message.Request import Request
from message.Response import Response
from message.StatusCode import StatusCode
import os
from handler.HandlerErrors import HandlerErrors
from databaseUser.HandlerDatabase import HandlerDatabase


class GET:
    urlTable = {
        "/": {"type": "text/html", "filePath": "./assets/public/index.html"},
        "/post": {"type": "text/html", "filePath": "./assets/public/post.html"},
        "/list": {"type": "text/html", "filePath": "./assets/public/list.html"},
        "/error": {"type": "text/html", "filePath": "./assets/public/error.html"},
        "/database": {"type": "application/json", "filePath": "./databaseUser/database.json"},
        "/bootstrap.min.css": {"type": "text/css", "filePath": "./assets/bootstrap.min.css"},
        "/dashboard.css": {"type": "text/css", "filePath": "./assets/dashboard.css"},
        "/popper.min.js": {"type": "text/css", "filePath": "./assets/popper.min.js"},
        "/bootstrap.min.js": {"type": "text/css", "filePath": "./assets/bootstrap.min.js"},
        "/edit": {"type": "text/html", "filePath": "./assets/put.html"},
    }
    imagesTable = {
        "/deusgrego.jpeg": {"type": "image/jpeg", "filePath": "./assets/static/deusgrego.jpeg"},

        "/slide1.jpg": {"type": "image/jpeg", "filePath": "./assets/static/slide1.jpg"},
        "/slide2.png": {"type": "image/png", "filePath": "./assets/static/slide2.png"},
        "/slide3.png": {"type": "image/png", "filePath": "./assets/static/slide3.png"},

        "/menu1.gif": {"type": "image/gif", "filePath": "./assets/static/menu1.gif"},
        "/menu2.gif": {"type": "image/gif", "filePath": "./assets/static/menu2.gif"},
        "/menu3.gif": {"type": "image/gif", "filePath": "./assets/static/menu3.gif"},

        "/error.gif": {"type": "image/gif", "filePath": "./assets/static/error.gif"},

        "/newfriend.jpeg": {"type": "image/jpeg", "filePath": "./assets/static/newfriend.jpeg"},

        "/logo.png": {"type": "image/png", "filePath": "./assets/static/logo.png"},
        "/logo.ico": {"type": "image/x-icon", "filePath": "./assets/static/logo.ico"},
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
        elif request.URI in GET.imagesTable:
            response: Response = Response(status_code=StatusCode.OK, body={}, header={})
            try:
                image = open(GET.imagesTable[request.URI]["filePath"], "rb")
                byte_image = image.read()
                response.body = byte_image
                response.headers["Content-Type"] = GET.imagesTable[request.URI]["type"]
                response.headers["Content-Length"] = str(os.stat(GET.imagesTable[request.URI]["filePath"]).st_size)
                response.headers["Accept-Ranges"] = "bytes"
            except Exception as e:
                print(e)

            return response.encodeResponseImages()

        return HandlerErrors.sendErrorCode(request, StatusCode.NOT_FOUND)

    @staticmethod
    def getParamsFromURL(url):
        parsedParams: dict = {}
        elements = url.split('?')[1].split('&')
        for elem in elements:
            splitElem = elem.split('=')
            parsedParams[splitElem[0]] = splitElem[1]

        return parsedParams
