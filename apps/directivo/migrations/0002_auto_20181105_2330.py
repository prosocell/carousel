# Generated by Django 2.0.2 on 2018-11-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directivo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunicadosalu',
            name='image',
        ),
        migrations.AddField(
            model_name='comunicadosalu',
            name='archivo',
            field=models.BinaryField(blank=True, null=True, verbose_name='Archivo'),
        ),
    ]
