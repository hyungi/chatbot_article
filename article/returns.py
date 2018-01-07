from . import lists

class Requesthandler:
    def __init__(self,press,date,category):
        self.press=press
        self.date=date
        self.category=category

    def setRequest(self,content):
        if content in lists.presslist :
            self.press = content
        elif content in lists.datelist :
            self.date = content
        elif content in lists.categorylist :
            self.category = content

    def resetRequest(self):
        self.press = ""
        self.date = ""
        self.category = ""

    def getRequest(self):
        return self.press,self.date,self.category
    
    def isFull(self):
        if len(self.press) == 0:
            return False
        elif len(self.date) == 0:
            return False
        elif len(self.category) == 0:
            return False
        else :
            return True
