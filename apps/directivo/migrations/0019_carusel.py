# Generated by Django 2.1.3 on 2018-12-20 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directivo', '0018_delete_caro'),
    ]

    operations = [
        migrations.CreateModel(
            name='carusel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('image', models.ImageField(upload_to='comalu', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'carusel',
                'verbose_name_plural': 'carusell',
                'ordering': ['-created'],
            },
        ),
    ]