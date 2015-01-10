# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_auto_20150110_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetail',
            options={'verbose_name': "Ligne d'une commande", 'verbose_name_plural': 'Lignes de commandes'},
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(to='commerce.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='short_desc',
            field=models.CharField(max_length=150, verbose_name=b'Description courte', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='default_invoicing_address',
            field=models.ForeignKey(related_name='default_invoicing_address', verbose_name=b'Adresse de facturation par d\xc3\xa9faut', to='commerce.Address', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='default_shipping_address',
            field=models.ForeignKey(related_name='default_shipping_address', verbose_name=b'Adresse de livraison par d\xc3\xa9faut', to='commerce.Address', null=True),
            preserve_default=True,
        ),
    ]
