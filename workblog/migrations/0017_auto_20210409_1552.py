# Generated by Django 3.1.7 on 2021-04-09 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workblog', '0016_auto_20210409_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workchart',
            name='datetime1',
            field=models.DateTimeField(null='True', verbose_name='datetime1'),
        ),
    ]
