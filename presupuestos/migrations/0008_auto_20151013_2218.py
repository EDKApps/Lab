# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0007_numerador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerador',
            name='nombre',
            field=models.CharField(unique=True, max_length=30, blank=b'true'),
        ),
    ]
