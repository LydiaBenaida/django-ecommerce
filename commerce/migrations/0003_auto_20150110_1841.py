# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0002_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Adresse', 'verbose_name_plural': 'Adresses'},
        ),
        migrations.AddField(
            model_name='client',
            name='default_invoicing_address',
            field=models.ForeignKey(related_name='invoicing_address', to='commerce.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='default_shipping_address',
            field=models.ForeignKey(related_name='shipping_address', to='commerce.Address', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='additional_address',
            field=models.CharField(max_length=255, verbose_name=b"Compl\xc3\xa9ment d'adresse", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=255, verbose_name=b'Adresse'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'Ville'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='company',
            field=models.CharField(max_length=50, verbose_name=b'Soci\xc3\xa9t\xc3\xa9', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=150, verbose_name=b'Pays'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='fax',
            field=models.CharField(max_length=10, verbose_name=b'Fax', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name=b'Pr\xc3\xa9nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='gender',
            field=models.CharField(default=b'MR', max_length=4, verbose_name=b'Civilit\xc3\xa9', choices=[(b'MR', b'Monsieur'), (b'MISS', b'Mademoiselle'), (b'MRS', b'Madame')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name=b'Nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='mobilephone',
            field=models.CharField(max_length=10, verbose_name=b'T\xc3\xa9l\xc3\xa9phone portable', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=10, verbose_name=b'T\xc3\xa9l\xc3\xa9phone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(max_length=5, verbose_name=b'Code postal'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='workphone',
            field=models.CharField(max_length=10, verbose_name=b'T\xc3\xa9l\xc3\xa9phone travail', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.ForeignKey(verbose_name=b'Utilisateur associ\xc3\xa9', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
