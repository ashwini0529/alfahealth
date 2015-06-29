# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='exerciseList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise_id', models.IntegerField(max_length=5)),
                ('exercise_name', models.CharField(max_length=256)),
                ('exercise_for', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='bmi',
            name='user_id',
            field=models.IntegerField(max_length=2),
        ),
    ]
