# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='fecha_de_aprobacion',
            field=models.DateField(verbose_name=b'fecha de aprobacion'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='fecha_de_solicitud',
            field=models.DateField(verbose_name=b'fecha de solicitud'),
        ),
    ]
