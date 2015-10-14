# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0004_presupuesto_fecha_de_vencimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto',
            name='fecha_de_vencimiento',
        ),
    ]
