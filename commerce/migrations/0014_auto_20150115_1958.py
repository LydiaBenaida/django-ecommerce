# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0013_auto_20150112_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='produit',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(upload_to=b'commerce/media', null=True, verbose_name=b'Miniature du produit'),
            preserve_default=True,
        ),
    ]
