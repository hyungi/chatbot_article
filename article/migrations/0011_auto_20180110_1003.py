# Generated by Django 2.0.1 on 2018-01-10 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_requirement_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='request_date',
            field=models.DateTimeField(default='2018-01-10 01:03'),
        ),
    ]