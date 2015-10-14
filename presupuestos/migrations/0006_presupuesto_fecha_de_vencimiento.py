# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0005_remove_presupuesto_fecha_de_vencimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='fecha_de_vencimiento',
            field=models.DateField(default=datetime.date.today, verbose_name=b'fecha de vencimiento'),
        ),
    ]
