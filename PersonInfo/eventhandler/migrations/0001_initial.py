# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_text', models.TextField(max_length=600)),
            ],
        ),
    ]
