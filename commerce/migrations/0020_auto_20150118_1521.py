# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0019_auto_20150118_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_date',
            field=models.DateField(null=True, verbose_name=b"Date de l'exp\xc3\xa9dition"),
            preserve_default=True,
        ),
    ]
