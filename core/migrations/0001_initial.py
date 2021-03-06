# Generated by Django 3.2.4 on 2021-06-18 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('idEspecialidad', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de la especialidad')),
                ('nombreEspecialidad', models.CharField(max_length=50, verbose_name='Nombre de la especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('nombre', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('edad', models.CharField(max_length=2, verbose_name='Edad')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.especialidad')),
            ],
        ),
    ]
