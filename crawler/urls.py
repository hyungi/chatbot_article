from django.conf.urls import url
from . import saveNews


urlpatterns = [
    url(r'^crawler/', saveNews.startcrawling),
]

'''
url 주소에 따라 적절한 view를 배정해줌.
'''

