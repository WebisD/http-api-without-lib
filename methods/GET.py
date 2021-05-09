from message.Request import Request
from message.Response import Response
from message.StatusCode import StatusCode
import os
from handler.HandlerErrors import HandlerErrors
from handler.HandlerImage import HandlerImage

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
        "/edit": {"type": "text/html", "filePath": "./assets/public/put.html"},
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
    def response(request: Request) -> str:
        """ Performs a return operation when there is a request of type GET, returning a response with
        the headers and the correct body. Search within the mapped URLs, the received URL, returning the requested resource.

        :param request: Request object, containing the body and headers of that request
        :returns: The answer to this request

        """
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
                    print("GET::response called " + request.URI +  " -> NOT_FOUND")
                    return HandlerErrors.sendErrorCode(request, StatusCode.NOT_FOUND)
            with open(GET.urlTable[request.URI]["filePath"], 'r', encoding='utf-8', errors='replace') as file:
                response.status_code = StatusCode.OK
                response.body = "".join(file.readlines())
                lastModified = Response.getDateFromSeconds(os.stat(file.name).st_mtime)

                response.headers["Last-Modified"] = lastModified
                response.headers["Content-Length"] = len(response.body)
                response.headers["Content-Type"] = GET.urlTable[request.URI]["type"]
                response.headers["Connection"] = "Closed"

            print("GET::response called " + request.URI +  " -> " + str(response.status_code))
            return response.encodeResponse()

        elif request.URI in GET.imagesTable:
            response: Response = Response(status_code=StatusCode.OK, body={}, header={})
            try:
                GET.fill_image_params(response, GET.imagesTable, request.URI)
            except Exception as e:
                print(e)
            
            print("GET::response called " + request.URI + " -> " + response.status_code.value[1])
            return response.encodeResponseImages()
        else:
            response: Response = Response(status_code=StatusCode.OK, body={}, header={})

            image_database = HandlerImage.getData()["images"]

            if image_database is None:
                response.status_code = StatusCode.INTERNAL_SERVER_ERROR
                print("GET::response called " + request.URI +  " -> INTERNAL_SERVER_ERROR")
                return response

            image = None
            for index, element in enumerate(image_database):
                if request.URI == list(element.keys())[0]:
                    image = element
                    break

            if image is not None:
                try:
                    GET.fill_image_params(response, image, request.URI)
                except Exception as e:
                    print(e)
                
                print("GET::response called " + request.URI +  " -> " + str(StatusCode.OK))
                return response.encodeResponseImages()

        print("GET::response called " + request.URI +  " -> NOT_FOUND")
        return HandlerErrors.sendErrorCode(request, StatusCode.NOT_FOUND)

    @staticmethod        
    def fill_image_params(response: Response, image_params: dict, uri: str) -> None:
        """ Add headers in response, based on image params
    
        :param response: Response 
        :param image_params: Dictionary with image params
        :param uri: String of URL 
        
        """
        image = open(image_params[uri]["filePath"], "rb")
        byte_image = image.read()
        response.body = byte_image
        response.headers["Content-Type"] = image_params[uri]["type"]
        response.headers["Content-Length"] = str(os.stat(image_params[uri]["filePath"]).st_size)
        response.headers["Accept-Ranges"] = "bytes"

    @staticmethod
    def getParamsFromURL(url):
        """ Performs a parse of the parameters present in the URL
    
        :param URI: String of the url
        :returns: A dictionary with all parameters contained in the URL
        
        """
        parsedParams: dict = {}
        elements = url.split('?')[1].split('&')
        for elem in elements:
            splitElem = elem.split('=')
            parsedParams[splitElem[0]] = splitElem[1]

        return parsedParams
