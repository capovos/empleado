# Generated by Django 3.2 on 2021-05-11 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=100, unique=True, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades del empleado',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_name', 'last_name')},
        ),
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
