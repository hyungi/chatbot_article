from django.contrib import admin
from .models import Requirement
from crawler.models import Document, DocumentSummary, SentimentList, Comment
admin.site.register(Document)
admin.site.register(DocumentSummary)
admin.site.register(SentimentList)
admin.site.register(Comment)
admin.site.register(Requirement)
# Register your models here.
