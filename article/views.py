from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

menulist = ['신문사 고르기', '날짜 고르기', '분야 고르기']

presslist = ['조선','중앙','동아',
        '경향','한겨레','한국경제','매일경제']

datelist = ['이틀전','어제','오늘']

categorylist= ['정치','경제','사회',
        '생활/문화','세계','IT/과학','오피니언']

selectedPress = None
selectedDate = None
selectedCategory = None

#고객의 요청 정보를 담을 객체 선언을 여기다 하자!
#request_list > answer.py 라는 걸 만들어서 여기다가 객체를 던져주고 요약한 것을 보내도록 하자

def keyboard(request):
    '''
    :param 카톡플친 API를 통해 넘어온 /keyboard request
    :return 카톡 플친 API를 적용할 때 필수적으로 요청하는 구성 요건으로
    json 값을 넘겨주기 위해 JsonResponse을 사용한다.
    '''
 
    return JsonResponse({
                'type' : 'buttons',
                'buttons' : menulist
                })

#content 로 받아진 내용을 저장할 수 있는 방법을 찾아야함
#세개의 객채를 구성해서 if문으로 구성해서 셋다 not null일 경우에는 선택이 완료되었음을 알리고 해당하는 정보를 전송함
#구성 된 세개의 정보 또한 json 화 해서 전송하자 예시 {'press':'조선','date':'어제','category':'세계'}

@csrf_exempt
def message(request):
    
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    content = return_json_str['content']
    #조건문을 통해서 '신문' 카테고리, '날짜'카테고리, '분야' 카테고리 인지 확인하도록 만들어야함. 
    if selectedPress is not None and selectedDate is not None :
        if selectedCategory is not None:
            return JsonResponse({
                'message':{
                    'text': "선택이 완료되었습니다!\n"+
                    "선택된 신문사: "+selectedPress+
                    "선택된 날짜: "+selectedDate+
                    "선택된 분야: "+selectedCategory 
                    },
                'keyboard':{
                    'type':'buttons',
                    'buttons': ['요청하기','다시선택하기']
                    }
                })
    elif content == u"요청하기":
        press = selectedPress
        date = selectedDate
        category = selectedCategory
        selectedDate = None
        selectedPress = None
        selectedCategory = None
        
        return JsonResponse({
            'message':{
                'text':"선택한 내용: "+
                "신문사: "+press+
                "날짜: "+date+
                "분야: "+category+
                "\n요약된 기사 내용"
                },
            'keyboard':{
                'type':'buttons',
                'buttons':menulist
                }
            })
    elif content == u"다시선택하기":
        return JsonResponse({
            'message':{
                'text':'다시 골라주세요!'
                },
            'keyboard': {
                'type': 'buttons',
                'buttons' : menulist
                }
            })
    elif content == u"신문사 고르기":
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
    else :
        return JsonResponse({
            'message': {
                'text': content +" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                },
            'keyboard': {
                'type': 'buttons',
                'buttons' : menulist
                }
            })
