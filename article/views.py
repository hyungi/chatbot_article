from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def keyboard(request):
    '''
    :param 카톡플친 API를 통해 넘어온 /keyboard request
    :return 카톡 플친 API를 적용할 때 필수적으로 요청하는 구성 요건으로
    json 값을 넘겨주기 위해 JsonResponse을 사용한다.
    '''
 
    return JsonResponse({
                'type' : 'buttons',
                'buttons' : [
                    '신문사 고르기', '날짜 고르기', '분야 고르기'
                    ]
                })
 
@csrf_exempt
def message(request):
        message = ((request.body).decode('utf-8'))
        return_json_str = json.loads(message)
        content = return_json_str['content']
        
        #조건문을 통해서 '신문' 카테고리, '날짜'카테고리, '분야' 카테고리 인지 확인하도록 만들어야함. 
        if content == u"신문사 고르기":
            return JsonResponse({
                    'message': {
                        'text': "신문사를 골라주세요!"
                    },
                    'keyboard': {
                        'type': 'buttons',
                            'buttons' : [
                            '조선','중앙','동아',
                            '경향','한겨레',
                            '한국경제','매일경제'
                            ]
                    }
            })
        elif content == u"날짜 고르기":
            return JsonResponse({
                    'message': {
                        'text': "날짜를 골라주세요!"
                        },
                    'keyboard': {
                        'type': 'buttons',
                            'buttons' : [
                            '이틀전','어제','오늘'
                            ]
                    }

                })
        elif content == u"분야 고르기":
            return JsonResponse({
                    'message': {
                        'text': "분야를 골라주세요!"
                        },
                    'keyboard': {
                        'type': 'buttons',
                            'buttons' : [
                            '정치','경제','사회','생활/문화','세계','IT/과학','오피니언'
                            ]
                    }

                })
        else :
            return JsonResponse({
                'message':{
                    'text': content +" 선택이 완료 되었습니다! 다른것을 선택해 보시겠어요?"
                    },
                    'buttons' : [
                    '신문사 고르기', '날짜 고르기', '분야 고르기'
                    ]
                })
