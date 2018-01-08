from django.conf.urls import url
from django.contrib import admin
from . import views, answer
from article.select import *

selector = select()

urlpatterns = [
        
        url(r'^keyboard/',views.keyboard),
#        url(r'^message',answer.message),
        url(r'^message',selector.message),
        url(r'^admin/',admin.site.urls),
        url(r'^friend$', views.add_friend),
        url(r'^friend/(?P<user_key>\w+)$', views.del_friend)

        ]

'''
url 주소에 따라 적절한 view를 배정해줌. 7행, 8행은 카카오톡 API를 위해 설정해둔것이고, 9행은 DB구성을 위해 설정함
'''

