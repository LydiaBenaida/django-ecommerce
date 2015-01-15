# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0011_auto_20150110_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='thumbnail',
            field=models.ForeignKey(verbose_name=b'Miniature du produit', to='commerce.Photo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to=b'commerce/'),
            preserve_default=True,
        ),
    ]
