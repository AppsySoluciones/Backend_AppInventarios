# Generated by Django 4.2.3 on 2023-07-24 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insumo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumo',
            name='grupo',
        ),
        migrations.AddField(
            model_name='insumo',
            name='certificacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Insumo.certificacion'),
        ),
        migrations.AlterField(
            model_name='certificacion',
            name='ingrediente_activo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Insumo.ingredienteactivo'),
        ),
        migrations.AlterField(
            model_name='certificacion',
            name='periodo_carencia',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='certificacion',
            name='periodo_reingreso',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='unidad_medida',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Insumo.unidadmedida'),
        ),
    ]