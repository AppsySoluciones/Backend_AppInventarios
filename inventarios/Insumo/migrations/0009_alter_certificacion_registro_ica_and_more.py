# Generated by Django 4.2.3 on 2023-12-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insumo', '0008_remove_certificacion_ingrediente_activo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificacion',
            name='registro_ica',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredienteactivo',
            name='nombre',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='unidadmedida',
            name='unidad',
            field=models.CharField(max_length=4, null=True, unique=True),
        ),
    ]