from server import *
from threading import Thread
from message.Request import Request
from message import Response, StatusCode
from databaseUser.ObjectUser import UserObj
from string import Template
import requests
import pathlib
from methods import GET
import json
import os

class HandlerImage:
   
    @staticmethod
    def saveImg(objUser):
        try:
            if(len(objUser.image) > 22):
                #HandlerImage.deleteImg(objUser.id, "/" + objUser.id + pathlib.Path(objUser.image))
                img_data = requests.get(objUser.image).content
                fileImg = "databaseUser/" + objUser.id + pathlib.Path(objUser.image).suffix

                with open(fileImg, 'wb') as handler:
                    handler.write(img_data)
        except:
            print("erro when save img")

    @staticmethod
    def deleteImg(objId, imageLink):
        print("A")
        #try:
        #    GET.GET.deleteImageLinkInGetList(imageLink)
        #    os.remove('databaseUser/' + objId + ".*")
        #except:
        #    print("erro when delete img")

    @staticmethod
    def addLinkImage(urlImage, extensionImage):
        GET.GET.addImageLinkInGetList(urlImage, extensionImage)

        try:
            with open('databaseUser/imagesLink.json', 'w') as f:
                json.dump(GET.GET.imagesTable, f)
        except:
            print("new image link not save")
