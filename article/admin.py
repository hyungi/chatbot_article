from django.contrib import admin
from .models import Document,Document_summary,Sentiment_list,Comment,Requirement

admin.site.register(Document)
admin.site.register(Document_summary)
admin.site.register(Sentiment_list)
admin.site.register(Comment)
admin.site.register(Requirement)
# Register your models here.
