# Generated by Django 5.0.1 on 2024-07-31 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_contribuyentes_regimenfiscal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=255)),
                ('archivo1', models.FileField(upload_to='archivos/')),
                ('archivo2', models.FileField(upload_to='archivos/')),
                ('archivo3', models.FileField(upload_to='archivos/')),
                ('archivo4', models.FileField(upload_to='archivos/')),
                ('archivo5', models.FileField(upload_to='archivos/')),
                ('contraseña', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_caducidad', models.DateField()),
            ],
        ),
    ]
