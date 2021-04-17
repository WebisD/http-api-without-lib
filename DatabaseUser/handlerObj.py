from server import *
from threading import Thread
from Message.request import Request

class HandlerObj():

    @staticmethod
    def get(msg):
       print("get")

    @staticmethod
    def put(msg):
        print("put")

    @staticmethod
    def post(msg):
       print("post")

    @staticmethod
    def delete(msg):
       print("delete")
