# Generated by Django 2.1.3 on 2018-12-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directivo', '0008_remove_comunicadosescolar_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicadosescolar',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='comalu', verbose_name='Imagen'),
        ),
    ]