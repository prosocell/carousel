# Generated by Django 2.1.3 on 2018-12-16 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directivo', '0014_auto_20181215_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunicadoescolar',
            name='archivo',
        ),
    ]
