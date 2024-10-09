# Generated by Django 5.0.1 on 2024-10-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tres_coelhos', '0005_remove_sorteiodupla_vaga_dupla_com'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartamento',
            name='apenas_dupla',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartamento',
            name='apenas_livre',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartamento',
            name='subsolo',
            field=models.IntegerField(blank=True, choices=[(1, 'Subsolo 1'), (2, 'Subsolo 2')], null=True),
        ),
    ]