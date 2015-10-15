# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0003_auto_20151012_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='fecha_de_vencimiento',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
