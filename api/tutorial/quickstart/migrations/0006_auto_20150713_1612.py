# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0005_auto_20150708_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='latitude',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='beacon',
            name='longitude',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
