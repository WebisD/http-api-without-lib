from Message.request import Request
from DatabaseUser.handlerDatabase import HandlerDatabase
from DatabaseUser.objectUser import UserObj
from Handler.handlerErrors import HandlerErrors
import json

class POST():
    @staticmethod
    def addObj(newObj):
        return HandlerDatabase.addNewObj(newObj)

    @staticmethod
    def response(request):
        data = json.loads(request.body)
        if data['name'] != "" and data['phone'] != "" and data['pokemon'] != "":
            obj = UserObj(data['name'], data['phone'], data['pokemon'])
            status = POST.addObj(obj)
            return status.encode()

        return HandlerErrors.sendErrorCode(request)