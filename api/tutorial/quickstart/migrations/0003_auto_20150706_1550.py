# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20150702_0641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beacon',
            name='name',
        ),
        migrations.AlterField(
            model_name='beacon',
            name='beacon_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
