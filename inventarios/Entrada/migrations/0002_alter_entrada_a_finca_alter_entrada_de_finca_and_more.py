# Generated by Django 4.2.3 on 2023-07-21 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fincas', '0002_remove_finca_email_remove_finca_propietario_and_more'),
        ('Insumo', '0001_initial'),
        ('Entrada', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='a_finca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas_a_finca', to='Fincas.finca'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='de_finca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas_de_finca', to='Fincas.finca'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insumo.insumo'),
        ),
    ]
