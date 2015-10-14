# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0002_auto_20151006_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_actual', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='estado',
            field=models.ForeignKey(to='presupuestos.Estado'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='tipo',
            field=models.ForeignKey(to='presupuestos.Tipo'),
        ),
    ]
