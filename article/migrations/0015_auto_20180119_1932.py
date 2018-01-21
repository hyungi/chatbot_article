# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20180117_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='request_date',
            field=models.DateTimeField(default='2018-01-19 10:32'),
        ),
    ]
