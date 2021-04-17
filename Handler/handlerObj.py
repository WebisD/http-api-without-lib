from server import *
from threading import Thread
from Message.request import Request

class HandlerObj():

    @staticmethod
    def get(msg):
       print("get")
       return true

    @staticmethod
    def put(msg):
        print("put")
       return true

    @staticmethod
    def post(msg):
       print("post")
       return true

    @staticmethod
    def delete(msg):
       print("delete")
       return true
