# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0018_auto_20150118_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_charge_id',
            field=models.CharField(max_length=30, verbose_name=b'Identifiant de transaction Stripe', blank=True),
            preserve_default=True,
        ),
    ]
