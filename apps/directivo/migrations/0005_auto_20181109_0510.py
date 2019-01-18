# Generated by Django 2.0.2 on 2018-11-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directivo', '0004_auto_20181106_0318'),
    ]

    operations = [
        migrations.CreateModel(
            name='comunicadosdoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='comalu', verbose_name='Archivo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Comunicados Docentes',
                'verbose_name_plural': 'Comunicados Docentes',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='comunicadosalu',
            options={'ordering': ['-created'], 'verbose_name': 'Comunicados Alumnos', 'verbose_name_plural': 'Comunicados Alumnos'},
        ),
    ]
