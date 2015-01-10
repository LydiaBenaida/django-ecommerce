# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0009_auto_20150110_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'')),
                ('produit', models.ForeignKey(to='commerce.Products')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
