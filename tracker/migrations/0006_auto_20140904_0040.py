# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0005_maincomment_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCommentTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='tracker.Comment')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='maincomment',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='maincomment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='maincomment',
            name='last_update',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='id',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='last_update',
        ),
        migrations.AddField(
            model_name='maincomment',
            name='comment_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=None, serialize=False, to='tracker.Comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='comment_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=None, serialize=False, to='tracker.Comment'),
            preserve_default=False,
        ),
    ]
