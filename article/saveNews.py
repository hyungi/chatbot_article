from article.models import *
from django.utils import timezone
import crawl.naver_news_crawler as cr
'''
article/saveNews.py
 
# Feedback 객체 생성
fb = Feedback(name = 'Kim', email = 'kim@test.com', comment='Hi', createDate=datetime.now())
 
# 새 객체 INSERT
fb.save()


'''

def saveDocument(idid,ipress,icategory,ipd,icd,ititle,itext,ilink,isentiment):
    '''
    각각의 데이터에 대응하는 input 데이터의 목록
    :param idid:
    :param ipress:
    :param icategory:
    :param ipd:
    :param icd:
    :param ititle:
    :param itext:
    :param ilink:
    :param isentiment:
    :return: 없음. DB에 .save() 를 통해 저장
    '''

    doc = Document(
            document_id=idid,
            press=ipress,
            category=icategory,
            published_date=ipd,
            crawled_date=icd,
            title=ititle,
            text=itext,
            link=ilink,
            sentiment=isentiment
    )
    doc.save()

def saveDocSummary(idid,is_n,it_rank,itw,itwc,itwt):
    docSum = Document_summary(document_id=idid,sentences_n=is_n,text_rank=it_rank,top_word=itw,top_word_count=itwc,top_word_tfidf=itwt)
    docSum.save()

def saveSentiment(idid,igood,iwarm,isad,iangry,iwant):
    sentiment = Sentiment_list(document_id=idid,good=igood,warm=iwarm,sad=isad,angry=iangry,want=iwant)
    sentiment.save()

def saveComment(idid,iuid,icontent,ipd,icd,irecomm,iunrecomm):
    comment = Comment(document_id=idid,user_id=iuid,content=icontent,published_date=ipd,crawled_date=icd,recomm = irecomm,unrecomm = iunrecomm)
    comment.save()

def saveReq(iuser_key,ipres,icategory,idate):
    requirement = Requirement(user_key=iuser_key,press=ipress,category=icategory,date=idate)
    requirement.save()


chrome_path = "/Users/seonghyeongi/python_projects/chatbot/crawl/chromedriver"
# chrome_path = "../crawl/chromedriver"

crawler = cr.crawler("2018-01-06")
print("before\n", crawler.date_list)
nd_doc_list, nd_summary_list, nd_comment_dict = crawler.naver_news_crawl()
print("after\n", crawler.date_list)

for i in nd_doc_list:
    saveDocument(nd_doc_list[i].document_id,
                 nd_doc_list[i].press,
                 nd_doc_list[i].category,
                 nd_doc_list[i].published_date,
                 nd_doc_list[i].crawled_date,
                 nd_doc_list[i].title,
                 nd_doc_list[i].text,
                 nd_doc_list[i].link,
                 nd_doc_list[i].sentiment,
                 )
