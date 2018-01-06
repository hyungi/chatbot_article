from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
import json
from . import lists

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
                'buttons' :list(menulist)
                })

#content 로 받아진 내용을 저장할 수 있는 방법을 찾아야함
#세개의 객채를 구성해서 if문으로 구성해서 셋다 not null일 경우에는 선택이 완료되었음을 알리고 해당하는 정보를 전송함
#구성 된 세개의 정보 또한 json 화 해서 전송하자 예시 {'press':'조선','date':'어제','category':'세계'}
#numSelected 를 통해 counting 하는게 제대로 작동 하지 않음 외부 변수를 사용하지 않고 데이터가 들어가 있는지 확인하는 방법을 강구해야함.
#세번째 선택이 끝났는데 바로 넘어가지 않고 어떤 버튼 이든 눌러야 다음으로 넘어가는 사항 수정이 필요함
#DB하고 연동하여 고객이 고른 정보에 맞춰 DB에서 맞는 정보를 끌어와서 보여주는 기능을 구현해야함

