# Generated by Django 5.0.1 on 2024-10-16 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sky_view', '0005_alter_vaga_tipo_vaga'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartamento',
            name='is_pne',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vaga',
            name='is_pne',
            field=models.BooleanField(default=False),
        ),
    ]
