from article.lists import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

class select:
    def __init__(self):
        self.press = None
        self.date = None
        self.category = None

    def setRequest(self,content):
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


    def message(self,request):

        message = ((request.body).decode('utf-8'))
        return_json_str = json.loads(message)
        content = return_json_str['content']
        user_key = return_json_str['user_key']
        
        if content == u"신문사 고르기":
            return JsonResponse({
                'message': {
                    'text': "신문사를 골라주세요!"
                    },
                'keyboard': {
                    'type': 'buttons',
                    'buttons' : list(presslist)
                    }
                })
        elif content == u"날짜 고르기":
            return JsonResponse({
                'message': {
                    'text': "날짜를 골라주세요!"
                    },
                'keyboard': {
                    'type': 'buttons',
                    'buttons' : list(datelist)
                    }
                })
        elif content == u"분야 고르기":
            return JsonResponse({
                'message': {
                    'text': "분야를 골라주세요!"
                    },
                'keyboard': {
                    'type': 'buttons',
                    'buttons' : list(categorylist)
                    }
                })
        else :
            self.setRequest(content)
            if self.isFull():
                RH.resetRequest()
                return JsonResponse({
                    'message':{
                        'text':"요청을 전송하였습니다."
                        },
                    'keyboard':{
                        'type': 'buttons',
                        'buttons': list(menulist)
                        }
                    })
            else :
                press,date,category = self.getRequest()
                result = None
                if press is not None:
                    result += "["+press+"]" 
                elif date is not None:
                    result += "["+date+"]"
                elif category is not None:
                    result += "["+category+"]"
            
                return JsonResponse({
                    'message': {
                        'text': result+" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                    },
                    'keyboard': {
                    'type': 'buttons',
                    'buttons' : list(menulist)
                        }
                    })

