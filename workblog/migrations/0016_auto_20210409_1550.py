# Generated by Django 3.1.7 on 2021-04-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workblog', '0015_auto_20210409_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workchart',
            name='datetime1',
            field=models.DateTimeField(verbose_name='datetime1'),
        ),
    ]
