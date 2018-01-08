from article.lists import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

class select:
    def __init__(self):
        self.press = ""
        self.date = ""
        self.category = ""

    def resetRequest(self):
        self.press = ""
        self.date = ""
        self.category = ""

    def getRequest(self):
        return self.press,self.date,self.category
#신문사 이름중 하나인지 확인
    def check_is_in_presslist(content):
        if content in presslist:
            return True
        else:
            return False
#날짜 목록중 하나인지 체크 -- 임시방편이라 수정해야함
    def check_is_in_datelist(content):
        if content in datelist:
            return True
        else:
            return False
#카테고리 중 하나인지 체크
    def check_is_in_categorylist(content):
        if content in categorylist:
            return True
        else:
            return False
#전부다 선택했는지 확인
    def is_Full(self):
        if self.press=="":
            return False
        elif self.date=="":
            return False
        elif self.category=="":
            return False
        else:
            return True


    def message(self,request):
        message = ((request.body).decode('utf-8'))
        return_json_str = json.loads(message)
        content = return_json_str['content']
        user_key = return_json_str['user_key']
    
        isPress = check_is_in_presslist(content)
        isDate = check_is_in_datelist(content)
        isCategory = check_is_in_categorylist(content)
    
    #요청하기가 들어오면 다른 .py 파일에서 불러온 기사 요약 정보를 보여줄 수 있도록 하자. 
    
        if content == u"신문사 고르기":
            return JsonResponse({
            'message': {
                'text': "신문사를 골라주세요!"
                },
            'keyboard': {
                'type': 'buttons',
                'buttons' : presslist
                }
            })
        elif content == u"날짜 고르기":
            return JsonResponse({
            'message': {
                'text': "날짜를 골라주세요!"
                },
            'keyboard': {
                'type': 'buttons',
                'buttons' : datelist
                }
            })
        elif content == u"분야 고르기":
            return JsonResponse({
            'message': {
                'text': "분야를 골라주세요!"
                },
            'keyboard': {
                'type': 'buttons',
                'buttons' : categorylist
                }
            })
        elif isPress:
            self.press = content
            
            if is_Full(self):
                result = ""
                result = self.press +", "+self.date+", "+self.category
                resetRequest(self)

                return JsonResponse({
                'message':{
                    'text':result+'선택이 모두 완료되었습니다.'
                    },
                'keyboard':{
                    'type':'buttons',
                    'buttons':menulist
                    }
                })
            else:
                return JsonResponse({
                'message': {
                    'text': self.press+", "+self.date+", "+self.category+" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                    },
                'keyboard': {
                'type': 'buttons',
                'buttons' : menulist
                    }
                })
        elif isDate:
            self.date = content
            
            if is_Full(self):
                result = ""
                result = self.press +", "+self.date+", "+self.category
                resetRequest(self) 
            
                return JsonResponse({
                'message':{
                    'text':result+'선택이 모두 완료되었습니다.'
                    },
                'keyboard':{
                    'type':'buttons',
                    'buttons':menulist
                    }
                })       
            else:
                return JsonResponse({
                    'message': {
                    'text': self.press+", "+self.date+", "+self.category+" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                    },
                    'keyboard': {
                    'type': 'buttons',
                    'buttons' : menulist
                    }
                })   
        elif isCategory:
            self.category = content
        
            if is_Full(self):
                result = ""
                result = self.press +", "+self.date+", "+self.category
            
                return JsonResponse({
                    'message':{
                        'text':result+'선택이 모두 완료되었습니다.'
                        },
                    'keyboard':{
                        'type':'buttons',
                        'buttons':menulist
                        }
                    })
        
            else:
            
                return JsonResponse({
                    'message': {
                    'text': self.press+", "+self.date+", "+self.category+" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                    },
                    'keyboard': {
                    'type': 'buttons',
                    'buttons' : menulist
                        }
                    }) 
        else :
        
            return JsonResponse({
                'message': {'text':'죄송합니다 정의되지 않은 응답입니다.'},
                'keyboard' : {
                    'type':'buttons',
                    'buttons' : menulist
                    }
                })

