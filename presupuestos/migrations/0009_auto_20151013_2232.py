# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0008_auto_20151013_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='numerador',
            old_name='Ultimo_valor',
            new_name='ultimo_valor',
        ),
    ]
