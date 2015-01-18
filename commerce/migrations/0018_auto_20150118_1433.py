# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0017_remove_address_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='total_price',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product_unit_price',
            field=models.FloatField(default=0, verbose_name=b'Prix unitaire du produit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='vat',
            field=models.FloatField(verbose_name=b'Taux de TVA'),
            preserve_default=True,
        ),
    ]
