# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20150220_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
    ]