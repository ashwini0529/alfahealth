# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bmi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name=b'max_length = 2')),
                ('bmi', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('desired_id', models.IntegerField(default=0)),
            ],
        ),
    ]
