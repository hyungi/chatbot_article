# Generated by Django 2.0.1 on 2018-01-20 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20180119_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='document_id',
        ),
        migrations.RemoveField(
            model_name='document_summary',
            name='document_id',
        ),
        migrations.RemoveField(
            model_name='sentiment_list',
            name='document_id',
        ),
        migrations.AlterField(
            model_name='requirement',
            name='request_date',
            field=models.DateTimeField(default='2018-01-20 03:40'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Document_summary',
        ),
        migrations.DeleteModel(
            name='Sentiment_list',
        ),
    ]