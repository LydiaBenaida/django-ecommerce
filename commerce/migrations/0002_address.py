# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(default=b'MR', max_length=4, choices=[(b'MR', b'Monsieur'), (b'MISS', b'Mademoiselle'), (b'MRS', b'Madame')])),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50, blank=True)),
                ('address', models.CharField(max_length=255)),
                ('additional_address', models.CharField(max_length=255, blank=True)),
                ('country', models.CharField(max_length=150)),
                ('postcode', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('mobilephone', models.CharField(max_length=10, blank=True)),
                ('fax', models.CharField(max_length=10, blank=True)),
                ('workphone', models.CharField(max_length=10, blank=True)),
                ('client', models.ForeignKey(to='commerce.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
