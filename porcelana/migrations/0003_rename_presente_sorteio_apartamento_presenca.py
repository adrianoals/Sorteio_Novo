# Generated by Django 5.0.1 on 2024-04-16 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porcelana', '0002_apartamento_presente_sorteio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartamento',
            old_name='presente_sorteio',
            new_name='presenca',
        ),
    ]