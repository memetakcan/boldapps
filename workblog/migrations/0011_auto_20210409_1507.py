# Generated by Django 3.1.7 on 2021-04-09 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workblog', '0010_auto_20210409_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workchart',
            name='datetime1',
            field=models.DateField(default=datetime.date(2021, 4, 9), verbose_name='datetime'),
        ),
    ]