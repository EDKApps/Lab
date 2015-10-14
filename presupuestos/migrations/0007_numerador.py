# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0006_presupuesto_fecha_de_vencimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numerador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30, blank=b'true')),
                ('Ultimo_valor', models.IntegerField(default=0)),
            ],
        ),
    ]
