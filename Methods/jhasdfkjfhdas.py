class POST:
    def __init__(self):
        self.URLHashTable = {}
        
    def addNewUrl(self, url, func):
        print(func)
        self.URLHashTable[url] = func


class Request:
    def __init__(self, uri, body):
        self.uri = uri
        self.body = body


class Response:
    def __init__(self):
        self.body = ""
    
    def send(self, content):
        self.body = content        


class Handler:
    def __init__(self, post):
        self.post = post
    
    def recv(self, request):
        response = Response()
        
        # aqui teria um if para checar o tipo de request
        self.post.URLHashTable[request.uri](request, response)
        

class HTTP:
    def __init__(self):
        self.postObj = POST()
        self.handler = Handler(self.postObj)
    
    def post(self, url, **func):
        def function_wrapper(func):
            self.postObj.addNewUrl(url, func)
        return function_wrapper
    
    def runServer(host='', port=8080):
        print(f"Server running on {host}:{port}")


def myFunc(request, response):
    print(d)

def main():
    
    http = HTTP()
    
    @http.post('/users')
    def createUser(request, response):
        db = {"data": {}}
        db["data"]["1"] = request.body
        html = "<h1>TUDO CERTO<h2>"
        print(html)
        response.send(html)
        print(db)
        
        return html
    
    # http.post('/users', (request, response) => :
    #     db["data"]["1"] = request.body
    #     html = "<h1>TUDO CERTO<h2>"
    #     print(html)
    #     reponse.send(html)
    # )
    
    print(http.postObj.URLHashTable)
    
    HTTP.runServer('localhost', 8080)
    
    request = Request('/users', "Antonio")
    http.handler.recv(request)



main()