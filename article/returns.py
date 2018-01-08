from article.models import *
from article.lists import *

class requestHandler:
    def __init__(self):
        self.press = None
        self.date = None
        self.category = None

    def setRequest(self,press,date,category):
        if content in presslist:
            self.press = content
        elif content in datelist:
            self.date = content
        elif content in categorylist:
            self.category = content
        
    def resetRequest(self):
        self.press = None
        self.date = None
        self.category = None

    def getRequest(self):
        return self.press,self.date,self.category

    def isFull(self):
        if self.press is None:
            return False
        elif self.category is None:
            return False
        elif self.date is None:
            return False
        else:
            return True

'''
class requestPusher:
    def pushRequest(user_key,content):
        rq = Requirement.objects.get(user_id = user_key)
        if content in presslist:
            rq.press = content
        elif content in categorylist:
            rq.category = content
        elif content in datelist:
            rq.date = content
        rq.save()
'''
