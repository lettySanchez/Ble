# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_beacon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='implement_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='beacon',
            name='tractor_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
