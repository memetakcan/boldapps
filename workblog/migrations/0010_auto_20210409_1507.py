# Generated by Django 3.1.7 on 2021-04-09 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workblog', '0009_auto_20210409_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workchart',
            name='datetime',
        ),
        migrations.AddField(
            model_name='workchart',
            name='datetime1',
            field=models.DateField(default=datetime.date.today, verbose_name='datetime'),
        ),
    ]
