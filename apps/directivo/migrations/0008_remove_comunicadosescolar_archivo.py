# Generated by Django 2.1.3 on 2018-12-04 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directivo', '0007_comunicadosescolar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunicadosescolar',
            name='archivo',
        ),
    ]
