# Generated by Django 2.0.1 on 2018-01-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20180107_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=200)),
                ('press', models.CharField(default='', max_length=200)),
                ('category', models.CharField(default='', max_length=200)),
                ('date', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
