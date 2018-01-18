from django.db import models
from django.utils import timezone
'''
/article/models.py

'''

class Document(models.Model):
    #author = models.ForeignKey(
    #        'auth.User',
    #        on_delete=models.DO_NOTHING,
    #        )
    document_id = models.CharField(
            max_length=50,
            primary_key=True,
            )
    press = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=50,null=True)
    published_date =  models.DateTimeField(default=timezone.now)
        # datetime.strptime(published_date, '%Y-%m-%d %H:%M')
    crawled_date = models.DateTimeField(default=timezone.now)
        # datetime.now().strftime("%Y-%m-%d %H:%M")
    title = models.TextField()
    text = models.TextField()
    link = models.URLField(default="https://") 
    
    def __str__(self):
        return self.title

class Document_summary(models.Model):
    
    document_id = models.OneToOneField(
            Document,
            on_delete=models.CASCADE,
            primary_key = True)
    sentences_n = models.IntegerField()
    text_rank = models.TextField()
    top_word = models.TextField()
    top_word_count = models.TextField()
    top_word_tfidf = models.TextField()

class Sentiment_list(models.Model):
    document_id = models.OneToOneField(
            Document,
            on_delete=models.CASCADE,
            primary_key = True)
    good = models.IntegerField()
    warm = models.IntegerField()
    sad = models.IntegerField()
    angry = models.IntegerField()
    want = models.IntegerField()

class Comment(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE) 
    user_id = models.CharField(max_length=100,default="")
    content = models.TextField()
    published_date = models.DateTimeField()
    crawled_date = models.DateTimeField()
    recomm = models.IntegerField()
    unrecomm = models.IntegerField()

class Requirement(models.Model):
    user_key = models.CharField(max_length=200,default="")
    press = models.CharField(max_length=200,default="")
    date = models.CharField(max_length=200,default="") 
    category = models.CharField(max_length=200,default="")
    request_date = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d %H:%M"))
    
    def __str__(self):
        return self.press+", " +self.date+", "+self.category
