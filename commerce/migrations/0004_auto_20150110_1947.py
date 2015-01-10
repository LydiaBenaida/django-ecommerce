# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_auto_20150110_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'Nom de la cat\xc3\xa9gorie')),
                ('short_desc', models.CharField(max_length=150, verbose_name=b'Description courte')),
                ('parent_category', models.ForeignKey(to='commerce.Category')),
            ],
            options={
                'verbose_name': 'Cat\xe9gorie de produits',
                'verbose_name_plural': 'Cat\xe9gories de produits',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_date', models.DateField(auto_now=True, verbose_name=b'Date de la commande')),
                ('shipping_date', models.DateField(verbose_name=b"Date de l'exp\xc3\xa9dition", blank=True)),
                ('status', models.CharField(default=b'W', max_length=1, verbose_name=b'Statut de la commande', choices=[(b'W', b'En attente de validation'), (b'P', b'Pay\xc3\xa9e'), (b'S', b'Exp\xc3\xa9di\xc3\xa9e'), (b'C', b'Annul\xc3\xa9e')])),
                ('price', models.FloatField(verbose_name=b'Montant total')),
                ('client', models.ForeignKey(verbose_name=b'Client ayant pass\xc3\xa9 commande', to='commerce.Client')),
                ('invoicing_address', models.ForeignKey(related_name='order_invoicing_address', to='commerce.Address')),
                ('shipping_address', models.ForeignKey(related_name='order_shipping_address', to='commerce.Address')),
            ],
            options={
                'verbose_name': 'Commande',
                'verbose_name_plural': 'Commandes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(verbose_name=b'Quantit\xc3\xa9')),
                ('price', models.FloatField(verbose_name=b'Prix HT')),
                ('vat', models.FloatField(verbose_name=b'TVA')),
                ('total_price', models.FloatField(verbose_name=b'Prix TTC')),
                ('order', models.ForeignKey(to='commerce.Order')),
            ],
            options={
                'verbose_name': 'Ligne dune commande',
                'verbose_name_plural': 'Lignes dune commande',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'Nom du produit')),
                ('short_desc', models.CharField(max_length=150, verbose_name=b'Description courte')),
                ('long_desc', models.TextField(verbose_name=b'Description longue')),
                ('price', models.FloatField(verbose_name=b'Prix HT du produit')),
                ('category', models.ForeignKey(to='commerce.Category')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VAT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percent', models.FloatField(verbose_name=b'Taux de TVA (d\xc3\xa9cimal)')),
            ],
            options={
                'verbose_name': 'Taux de TVA',
                'verbose_name_plural': 'Taux de TVA',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='products',
            name='vat',
            field=models.ForeignKey(to='commerce.VAT'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(to='commerce.Products'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='default_invoicing_address',
            field=models.ForeignKey(related_name='default_invoicing_address', to='commerce.Address', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='default_shipping_address',
            field=models.ForeignKey(related_name='default_shipping_address', to='commerce.Address', null=True),
            preserve_default=True,
        ),
    ]
