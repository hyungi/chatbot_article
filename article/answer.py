from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from article.lists import *
from article.getNews import *
from article.models import *
'''
/article/answer.py

'''
press={}
date={}
category={}


@csrf_exempt
def message(request):
    global press
    global date
    global category

    '''
    :param 고객이 버튼을 눌렀을 경우 작동하는 함수로아래와 같은 정보가 전달된다.
    user_key: reqest.body.user_key, //user_key
    type: reqest.body.type,            //메시지 타입
    content: reqest.body.content    //메시지 내용
    :return JsonResponse를 통해 message 와 keyboard(optional)가 반환된다.
    '''
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
        press[user_key] = content
        print("here is isPres"+ press[user_key])
        
        if is_Full(user_key):
            print("press and Full")
            result = ""
            result = press[user_key] +", "+date[user_key]+", "+category[user_key]

            rq = Requirement(user_key=user_key,press=press[user_key],date=date[user_key],category=category[user_key])
            rq.save()
            news_list = getNews(press[user_key],date[user_key],category[user_key])
            print(news_list)
            del press[user_key]
            del date[user_key]
            del category[user_key]
            
            return JsonResponse({
                'message':{
                    'text':result+'선택이 모두 완료되었습니다.'+news_list
                    },
                'keyboard':{
                    'type':'buttons',
                    'buttons':menulist
                    }
                })
        else:
            result = press.get(user_key)
            if date.get(user_key) is not None:
                result += "/"
                result += date.get(user_key)
            if category.get(user_key) is not None:
                result += "/"
                result += category.get(user_key)
                
            return JsonResponse({
                'message': {
                    'text': result+" 선택이 완료 되었습니다! 날짜를 택해 보시겠어요?"
                    },
                'keyboard': {
                'type': 'buttons',
                'buttons' : datelist
                    }
                })
    elif isDate:
        date[user_key] = content
        print("here is isDate"+ date[user_key])
        
        if is_Full(user_key):
            print("date and Full")
            result = ""
            result = press[user_key] +", "+date[user_key]+", "+category[user_key]
            rq = Requirement(user_key=user_key,press=press[user_key],date=date[user_key],category=category[user_key])
            rq.save()
            news_list = getNews(press[user_key],date[user_key],category[user_key])

            del press[user_key]
            del date[user_key]
            del category[user_key]
            
            news_list = getNews(press[user_key],date[user_key],category[user_key])

            print(news_list)

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
            result = ""
            if press.get(user_key) is not None:
                result += press.get(user_key)
            if date.get(user_key) is not None:
                result += "/"
                result += date.get(user_key)
            if category.get(user_key) is not None:
                result += "/"
                result += category.get(user_key)
            return JsonResponse({
            'message': {
                'text': result+" 선택이 완료 되었습니다! 분야를 선택해 보시겠어요?"
                },
            'keyboard': {
            'type': 'buttons',
            'buttons' : categorylist
                }
            })   
    
    elif isCategory:
        category[user_key] = content
        print("here is isCategory"+ category[user_key])
        
        if is_Full(user_key):
            print("Category and Full")
            result = ""
            result = press[user_key] +", "+date[user_key]+", "+category[user_key]
            
            #고객의 요청에 맞는 내용을 불러오는 코드를 작성해야함
            rq = Requirement(user_key=user_key,press=press[user_key],date=date[user_key],category=category[user_key])
            rq.save()
            news_list = getNews(press[user_key],date[user_key],category[user_key])
            print(news_list)
            del press[user_key]
            del date[user_key]
            del category[user_key]
            
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
            result = ""
            if press.get(user_key) is not None:
                result += press.get(user_key)
            if date.get(user_key) is not None:
                result += date.get(user_key)
            if category.get(user_key) is not None:
                result += category.get(user_key)
            
            return JsonResponse({
                'message': {
                    'text': result+" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                    },
                'keyboard': {
                'type': 'buttons',
                'buttons' : menulist
                    }
                }) 
    else :
        print("정의되지 않은 구문")
        return JsonResponse({
            'message': {'text':'죄송합니다 정의되지 않은 응답입니다.'},
            'keyboard' : {
                'type':'buttons',
                'buttons' : menulist
                }
            })
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
def is_Full(user_key):
    global press
    global date
    global category
    
    if press.get(user_key) is None:
        return False
    elif date.get(user_key) is None:
        return False
    elif category.get(user_key) is None:
        return False
    else:
        return True

