# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonInfoSite', '0003_person_person_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_picture',
            new_name='person_pic',
        ),
    ]