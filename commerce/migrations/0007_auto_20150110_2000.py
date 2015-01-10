# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0006_auto_20150110_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(verbose_name=b'Cat\xc3\xa9gorie parente', blank=True, to='commerce.Category'),
            preserve_default=True,
        ),
    ]
