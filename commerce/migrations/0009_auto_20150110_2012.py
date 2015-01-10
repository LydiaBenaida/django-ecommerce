# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_auto_20150110_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='invoicing_address',
            field=models.ForeignKey(related_name='order_invoicing_address', verbose_name=b'Adresse de facturation', to='commerce.Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(related_name='order_shipping_address', verbose_name=b'Adresse de livraison', to='commerce.Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(verbose_name=b'Commande associ\xc3\xa9e', to='commerce.Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(verbose_name=b'Cat\xc3\xa9gorie du produit', to='commerce.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='products',
            name='vat',
            field=models.ForeignKey(verbose_name=b'Taux de TVA', to='commerce.VAT'),
            preserve_default=True,
        ),
    ]
