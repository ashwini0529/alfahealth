# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfa', '0002_auto_20150629_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmi',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exerciselist',
            name='exercise_id',
            field=models.IntegerField(),
        ),
    ]
