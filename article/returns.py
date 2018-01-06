from . import lists

class Requesthandler:
    def __init__(self,press,date,category,length):
        self.press=press
        self.date=date
        self.category=category
        self.length = length

    def setRequest(self,content):
        if content in lists.presslist :
            self.press = content
            self.length+=1
        elif content in lists.datelist :
            self.date = content
            self.length+=1
        elif content in lists.categorylist :
            self.category = content
            self.length+=1

    def resetRequest(self):
        self.press = ""
        self.date = ""
        self.category = ""
        self.length = 0

    def getRequest(self):
        return self.press,self.date,self.category
    def isFull(self):
        if self.length == 3:
            return True
        else :
            return False
#    def getLength(self):
#        return self.length

