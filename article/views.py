from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
 
def keyboard(request):
 
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : [
                    '조선','중앙','동아',
                    '경향','한겨레',
                    '한국경제','매일경제'
                    ]
                })
 
@csrf_exempt
def message(request):
        message = ((request.body).decode('utf-8'))
        return_json_str = json.loads(message)
        return_str = return_json_str['content']
 
        return JsonResponse({
                'message': {
                    'text': "you push this button: "+return_str+"!"
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

