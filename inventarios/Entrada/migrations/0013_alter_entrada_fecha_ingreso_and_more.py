# Generated by Django 4.2.3 on 2023-08-22 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0012_alter_entrada_fecha_ingreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 17, 59, 31, 851448)),
        ),
        migrations.AlterField(
            model_name='historicalentrada',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 17, 59, 31, 851448)),
        ),
    ]
