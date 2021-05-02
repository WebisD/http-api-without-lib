from server import *
from threading import Thread
from message.Request import Request
from message import Response, StatusCode
from string import Template
import requests
import pathlib
from methods import GET
import json

class HandlerImage:
   
    @staticmethod
    def saveImg(objUser):
        img_data = requests.get(objUser.image).content
        fileImg = "databaseUser/" + objUser.id + pathlib.Path(objUser.image).suffix

        with open(fileImg, 'wb') as handler:
            handler.write(img_data)

    @staticmethod
    def addLinkImage(urlImage, extensionImage):
        GET.GET.addImageLinkInGetList(urlImage, extensionImage )

        try:
            with open('databaseUser/imagesLink.json', 'w') as f:
                json.dump(GET.GET.imagesTable, f)
        except:
            print("new image link not save")
