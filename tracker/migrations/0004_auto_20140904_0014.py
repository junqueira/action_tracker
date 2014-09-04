# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_taskdependency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
