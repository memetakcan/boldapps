# Generated by Django 3.1.7 on 2021-04-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workblog', '0008_remove_workchart_metin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workchart',
            name='datetime',
            field=models.CharField(max_length=120, verbose_name='Tarih'),
        ),
    ]
