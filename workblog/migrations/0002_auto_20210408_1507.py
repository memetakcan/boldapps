# Generated by Django 3.1.7 on 2021-04-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workchart',
            name='metin',
            field=models.CharField(choices=[('denenme', 'deneme2'), ('deneme3', 'deneme4')], max_length=120, verbose_name='projeler'),
        ),
    ]
