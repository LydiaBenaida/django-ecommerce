# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0016_auto_20150117_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
    ]
