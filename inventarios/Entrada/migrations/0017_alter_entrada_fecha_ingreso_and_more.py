# Generated by Django 4.2.3 on 2023-08-28 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0016_alter_entrada_fecha_ingreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 28, 7, 28, 31, 644604)),
        ),
        migrations.AlterField(
            model_name='historicalentrada',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 28, 7, 28, 31, 644604)),
        ),
    ]
