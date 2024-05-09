# Generated by Django 5.0.1 on 2024-05-09 03:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helbor', '0005_apartamentotorre2_vagatorre2_sorteiotorre2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteiotorre2',
            name='apartamento',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='helbor.apartamentotorre2'),
        ),
        migrations.AlterField(
            model_name='sorteiotorre2',
            name='vaga',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='helbor.vagatorre2'),
        ),
    ]