# Generated by Django 2.1.3 on 2018-12-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clacentro', models.CharField(blank=True, max_length=45, null=True)),
                ('nombreplan', models.CharField(blank=True, max_length=45, null=True)),
                ('clavestado', models.CharField(blank=True, max_length=45, null=True)),
                ('clavemuni', models.CharField(blank=True, max_length=45, null=True)),
                ('clavelocal', models.CharField(blank=True, max_length=45, null=True)),
                ('matricula', models.CharField(blank=True, max_length=45, null=True)),
                ('nombres', models.CharField(blank=True, max_length=45, null=True)),
                ('papellido', models.CharField(blank=True, max_length=45, null=True)),
                ('sapellido', models.CharField(blank=True, max_length=45, null=True)),
                ('curp', models.CharField(blank=True, max_length=45, null=True)),
                ('telcasa', models.CharField(blank=True, max_length=45, null=True)),
                ('grado', models.CharField(blank=True, max_length=45, null=True)),
                ('grupo', models.CharField(blank=True, max_length=45, null=True)),
                ('orden', models.CharField(blank=True, max_length=45, null=True)),
                ('claveplan', models.CharField(blank=True, max_length=45, null=True)),
                ('clavemate', models.CharField(blank=True, max_length=45, null=True)),
                ('materia', models.CharField(blank=True, max_length=45, null=True)),
                ('semestre', models.CharField(blank=True, max_length=45, null=True)),
                ('clavegrupo', models.CharField(blank=True, max_length=4, null=True)),
                ('turno', models.CharField(blank=True, max_length=45, null=True)),
                ('parcial_1', models.CharField(blank=True, max_length=45, null=True)),
                ('parcial_2', models.CharField(blank=True, max_length=45, null=True)),
                ('parcial_3', models.CharField(blank=True, max_length=45, null=True)),
                ('calificaci', models.CharField(blank=True, max_length=45, null=True)),
                ('prompar', models.CharField(blank=True, max_length=45, null=True)),
                ('promsem', models.CharField(blank=True, max_length=45, null=True)),
                ('inasistenc', models.CharField(blank=True, max_length=45, null=True)),
                ('numclases', models.CharField(blank=True, max_length=45, null=True)),
                ('inasispar1', models.CharField(blank=True, max_length=45, null=True)),
                ('nclasespar', models.CharField(blank=True, max_length=45, null=True)),
                ('inasispar2', models.CharField(blank=True, max_length=45, null=True)),
                ('nclasespa2', models.CharField(blank=True, max_length=45, null=True)),
                ('inasispar3', models.CharField(blank=True, max_length=45, null=True)),
                ('nclasespa3', models.CharField(blank=True, max_length=45, null=True)),
                ('edoacredit', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='alumno',
        ),
    ]
