# Generated by Django 5.0.1 on 2024-04-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porcelana', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartamento',
            name='presente_sorteio',
            field=models.BooleanField(default=False),
        ),
    ]
