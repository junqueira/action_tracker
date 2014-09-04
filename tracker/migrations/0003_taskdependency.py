# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_taskassignedto_taskowner'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDependency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('dependent_task', models.ForeignKey(related_name=b'dependent_task', to='tracker.Task')),
                ('depends_on', models.ForeignKey(related_name=b'depends_on', to='tracker.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
