# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20150706_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
