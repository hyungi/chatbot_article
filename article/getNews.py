from article.models import *
from article.lists import *
from django.utils import timezone
from datetime import datetime, date, time, timedelta

'''
/article/getNews.py

'''

def getNews(inputPress,inputYear,inputMonth,inputDay,inputCategory):

    '''
    :params
    고객이 입력한 press, date, category 정보를 바탕으로
    이에 맞는 뉴스 정보를 되돌려주는 함수
    
    :returns
    쿼리문에 의해 골라진 쿼리셋을 list 자료형으로 
    casting 하여 리턴한다.
    '''
    
    document = Document.objects.filter(press=inputPress)
    document = document.filter(category=inputCategory)
    document = document.filter(published_date__year=inputYear)
    document = document.filter(published_date__month=inputMonth)
    document = document.filter(published_date__day=inputDay)

    return_document = document.values('title','text')
    document_list = list(return_document)
    return document_list

