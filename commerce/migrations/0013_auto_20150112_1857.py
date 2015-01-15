# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0012_auto_20150112_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Miniature du produit'),
            preserve_default=True,
        ),
    ]
