# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0002_auto_20151006_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='referencia_clave',
            field=models.CharField(max_length=100, blank=b'true'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='referencia',
            field=models.CharField(max_length=20, blank=b'true'),
        ),
    ]
