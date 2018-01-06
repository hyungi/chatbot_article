from . import lists

class Requesthandler:
    def __init__(self,press,date,category,length):
        self.press=press
        self.date=date
        self.category=category
        self.length = length

    def setRequest(content):
        if content in presslist :
            self.press = content
            length = length + 1
        elif content in datelist :
            self.date = content
            length = length + 1
        elif content in categorylist :
            self.category = content
            length = length + 1

    def resetRequest():
        self.press = ""
        self.date = ""
        self.category = ""
        self.length = 0

    def getRequest():
        return self.press,self.date,self.category
    def isFull():
        if length == 3:
            return true
        else :
            return false
    def getLength():
        return self.length

