# Generated by Django 2.0.1 on 2018-01-07 05:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_remove_post_summarized_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='aId',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='crawled_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 7, 5, 47, 41, 996379, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='press',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 7, 5, 47, 41, 996349, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(),
        ),
    ]
