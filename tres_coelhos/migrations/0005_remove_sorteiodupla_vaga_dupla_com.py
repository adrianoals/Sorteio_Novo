# Generated by Django 5.0.1 on 2024-10-08 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tres_coelhos', '0004_sorteiodupla_vaga_dupla_com'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sorteiodupla',
            name='vaga_dupla_com',
        ),
    ]
