# Generated by Django 4.2.3 on 2023-08-01 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insumo', '0002_remove_insumo_grupo_insumo_certificacion_and_more'),
        ('Fincas', '0002_remove_finca_email_remove_finca_propietario_and_more'),
        ('Salida', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salida',
            name='existencia',
        ),
        migrations.RemoveField(
            model_name='salida',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='salida',
            name='medida',
        ),
        migrations.AlterField(
            model_name='salida',
            name='a_finca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidas_a_finca', to='Fincas.finca'),
        ),
        migrations.AlterField(
            model_name='salida',
            name='cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='salida',
            name='de_finca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidas_de_finca', to='Fincas.finca'),
        ),
        migrations.AlterField(
            model_name='salida',
            name='insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insumo.insumo'),
        ),
        migrations.AlterField(
            model_name='salida',
            name='semana',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='salida',
            name='total_entra_a_la_finca',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='salida',
            name='valor_unitario_entrada_a',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='salida',
            name='valor_unitario_salida',
            field=models.FloatField(default=0),
        ),
    ]
