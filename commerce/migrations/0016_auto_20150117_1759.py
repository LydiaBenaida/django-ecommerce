# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0015_auto_20150115_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('client', models.ForeignKey(to='commerce.Client')),
            ],
            options={
                'verbose_name': "Ligne d'un panier client",
                'verbose_name_plural': "Lignes d'un panier client",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'Nom du produit')),
                ('short_desc', models.CharField(max_length=150, verbose_name=b'Description courte')),
                ('long_desc', models.TextField(verbose_name=b'Description longue')),
                ('price', models.FloatField(verbose_name=b'Prix HT du produit')),
                ('thumbnail', models.ImageField(upload_to=b'commerce/media', null=True, verbose_name=b'Miniature du produit')),
                ('category', models.ForeignKey(verbose_name=b'Cat\xc3\xa9gorie du produit', to='commerce.Category')),
                ('vat', models.ForeignKey(verbose_name=b'Taux de TVA', to='commerce.VAT')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='vat',
        ),
        migrations.AddField(
            model_name='cartline',
            name='product',
            field=models.ForeignKey(to='commerce.Product'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(to='commerce.Product'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(to='commerce.Product'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
