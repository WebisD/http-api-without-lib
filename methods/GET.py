from message.Request import Request

class GET():
    urlTable = {
        "/": {"type": "text/html", "filePath": "./assets/index.html"},
        "/bootstrap.min.css": {"type": "text/css", "filePath": "./assets/bootstrap.min.css"},
        "/dashboard.css": {"type": "text/css", "filePath": "./assets/dashboard.css"},
        "/bootstrap-4.0.0/assets/js/vendor/popper.min.js": {"type": "text/css", "filePath": "./assets/bootstrap-4.0.0/assets/js/vendor/popper.min.js"},
        "/bootstrap-4.0.0/dist/js/bootstrap.min.js": {"type": "text/css", "filePath": "./assets/bootstrap-4.0.0/dist/js/bootstrap.min.js"},
        "/favicon.ico": {"type": "text/css", "filePath": "./assets/bootstrap-4.0.0/favicon.ico"},
        
    }

    @staticmethod
    def response(request):
<<<<<<< HEAD:Methods/GET.py
        response = f'''
HTTP/1.1 200 OK
Accept: text/html,text/css,text/javascript
Content-Type: {GET.urlTable[request.URI]["type"]}; charset:utf-8
'''
        with open(GET.urlTable[request.URI]["filePath"], 'r', encoding='utf-8') as file:
            response += "".join(file.readlines())
=======
        print("to aqui")
        response = ""
>>>>>>> adeb31972402f05ba285ea5f9ab7c6c7254bc6cf:methods/GET.py
        return response.encode()
