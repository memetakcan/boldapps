# Generated by Django 3.1.7 on 2021-04-09 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workblog', '0004_workchart_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='workchart',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Tarih'),
            preserve_default=False,
        ),
    ]
