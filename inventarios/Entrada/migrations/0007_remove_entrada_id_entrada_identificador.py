# Generated by Django 4.2.3 on 2023-08-01 21:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0006_remove_entrada_valor_unitario_salida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='id',
        ),
        migrations.AddField(
            model_name='entrada',
            name='identificador',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
