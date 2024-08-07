# Generated by Django 5.0.1 on 2024-07-03 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('max_club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartamentoBike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_apartamento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VagaBike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaga', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SorteioBike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartamento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='max_club.apartamento')),
                ('vaga', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='max_club.vaga')),
            ],
        ),
    ]
