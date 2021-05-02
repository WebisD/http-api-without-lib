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
    def saveImg(objUser: UserObj):
        try:
            if(len(objUser.image) > 22):
                img_data = requests.get(objUser.image).content
                fileName = str(objUser.id) + str((pathlib.Path(objUser.image).suffix))

                fileImg = "databaseUser/" + fileName
                with open(fileImg, 'wb') as handler:
                    handler.write(img_data)
        except:
            print("erro when save img")

    @staticmethod
    def deleteImg(objId, imageLink):
        try:
            HandlerImage.deleteLinkImage(imageLink)
            os.remove('databaseUser/' + str(objId) + ".*")
        except:
            print("erro when delete img")

    @staticmethod
    def addLinkImage(urlImage, extensionImage):
        GET.GET.addImageLinkInGetList(urlImage, extensionImage)

        try:
            with open('databaseUser/imagesLink.json', 'w') as f:
                json.dump(GET.GET.imagesTable, f)
        except:
            print("new image link not save")

    @staticmethod
    def deleteLinkImage(urlImage):
        GET.GET.deleteImageLinkInGetList(urlImage)
        try:
            with open('databaseUser/imagesLink.json', 'w') as f:
                json.dump(GET.GET.imagesTable, f)
        except:
            print("new image link not save")
