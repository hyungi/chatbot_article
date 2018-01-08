from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from article.lists import *
from article.returns import *
#lists 의 모든 리스트는 set자료형임

press=None
date=None
category=None

@csrf_exempt
def message(request):
    global press
    global date
    global category

    '''
    user_key: reqest.body.user_key, //user_key
    type: reqest.body.type,            //메시지 타입
    content: reqest.body.content    //메시지 내용
    '''
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    content = return_json_str['content']
    user_key = return_json_str['user_key']
    #요청하기가 들어오면 다른 .py 파일에서 불러온 기사 요약 정보를 보여줄 수 있도록 하자. 
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
    elif content in presslist:
        press = content
        return JsonResponse({
            'message': {
                'text': press+", "+date+", "+category+" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                },
            'keyboard': {
            'type': 'buttons',
            'buttons' : list(menulist)
                }
            })
    elif content in datelist:
        date = content
        return JsonResponse({
            'message': {
                'text': press+", "+date+", "+category+" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                },
            'keyboard': {
            'type': 'buttons',
            'buttons' : list(menulist)
                }
            })   
    else:
        category = content
        return JsonResponse({
            'message': {
                'text': press+", "+date+", "+category+" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                },
            'keyboard': {
            'type': 'buttons',
            'buttons' : list(menulist)
                }
            })     
