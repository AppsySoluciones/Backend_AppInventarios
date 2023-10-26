# Generated by Django 4.2.3 on 2023-07-18 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente_activo', models.CharField(max_length=100, null=True)),
                ('periodo_carencia', models.DateTimeField()),
                ('periodo_reingreso', models.DateTimeField()),
                ('registro_ica', models.CharField(max_length=50, null=True)),
                ('fecha_registro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='IngredienteActivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('unidad_medida', models.CharField(max_length=50, null=True)),
                ('grupo', models.CharField(max_length=100, null=True)),
                ('codigo_contable', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('inicial', models.CharField(max_length=5, null=True)),
                ('insumos', models.ManyToManyField(null=True, related_name='grupos', to='Insumo.insumo')),
            ],
        ),
    ]
