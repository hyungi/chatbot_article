from article.models import *
from article.lists import *
from django.utils import timezone
from datetime import datetime, date, time, timedelta

'''
/article/getNews.py

'''

def getNews(inputPress,inputDate,inputCategory):

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
    curDatetime = timezone.now()



    '''
    
    '''
    if(inputDate == "오늘"):
        print("inputDate is: " + inputDate)
        document = document.filter(published_date__date=curDatetime)

    elif(inputDate == "어제"):
        print("inputDate is: "+inputDate)
        curDatetime -= timezone.timedelta(days=1)
        document = document.filter(published_date__date=curDatetime)

    else:
        print("inputDate is: " + inputDate)
        curDatetime -= timezone.timedelta(days=2)
        document = document.filter(published_date__date=curDatetime)

    print(curDatetime.strftime("%Y-%m-%d %H:%M"))
    
    return_document = document.values('title','text')
    document_list = list(return_document)
    return document_list

'''
document = document.filter(published_date__year=datetime.date.today().strptime("%Y")
        document = document.filter(published_date__month=datetime.date.today().strptime("%m"))
        document = document.filter(published_date__day=datetime.date.today().strptime("%d"))
'''



#임시방편으로 짠 date 이며, 고른날짜에 따라 입력이 가능하도록 다시 만들어야함
