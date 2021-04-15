from server import *
from threading import Thread
from Handler import requestParser
from Message.request import Request


class Handler(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

    def run(self):
        while True:
            connectionSocket, addr = self.server.serverSocket.accept()
            
            while True:
                request = connectionSocket.recv(1024).decode()
        
                if not request: 
                    break
                else:
                    requestObj = requestParser.parse(request)
                    print(requestObj)
                    msg = Request(requestObj)
                    print(msg)
                    self.temporaryResponse(connectionSocket, requestObj)
                    break
                   
            print("close connection...")
            connectionSocket.close()
            break

    def temporaryResponse(self, connectionSocket, request_headers):
        response_body = [
            '<html><body><h1>Hello, world!</h1>',
            '<p>This page is in location %s, was requested ' % request_headers['Request-URI'],
            'using %s, and with HTTP %s.</p>' % (request_headers['Request-Type'], request_headers['HTTP-Version']),
            '<p>Request body is %s</p>' % request_headers['body'],
            '<p>Actual set of headers received:</p>',
            '<ul>',
        ]

        for request_header_name, request_header_value in request_headers.items():
            response_body.append('<li><b>%r</b> == %r</li>' % (request_header_name,
                                                               request_header_value))

        response_body.append('</ul></body></html>')

        response_body_raw = ''.join(response_body)

        # Clearly state that connection will be closed after this response,
        # and specify length of response body
        response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(response_body_raw),
            'Connection': 'close',
        }

        response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in \
                                       response_headers.items())

        # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
        response_proto = 'HTTP/1.1'.encode()
        response_status = '200'.encode()
        response_status_text = 'OK'.encode()  # this can be random

        # sending all this stuff
        connectionSocket.send(b'%s %s %s' % (response_proto, response_status,
                                        response_status_text))
        connectionSocket.send(response_headers_raw.encode())
        connectionSocket.send(b'\n')  # to separate headers from body
        connectionSocket.send(response_body_raw.encode())
