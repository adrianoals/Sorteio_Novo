from django.db import models

class ListaDePresenca(models.Model):
    APARTAMENTO_CHOICES = [
        ('Apto 01', 'apartamento 01'),
        ('Apto 02', 'apartamento 02'),
        ('Apto 03', 'apartamento 03'),
        ('Apto 04', 'apartamento 04'),
        ('Apto 05', 'apartamento 05'),
        # Adicione mais opções aqui
    ]

    VAGA_CHOICES = [
        ('Vaga 01', 'Vaga 01'),
        ('Vaga 02', 'Vaga 02'),
        ('Vaga 03', 'Vaga 03'),
        ('Vaga 04', 'Vaga 04'),
        ('Vaga 05', 'Vaga 05'),
        # Adicione mais opções aqui
    ]

    apartamento = models.CharField(max_length=100, choices=APARTAMENTO_CHOICES)
    bloco = models.CharField(max_length=100, default="-")
    presenca = models.BooleanField(default=False, null=True)
    vaga = models.CharField(max_length=100, choices=VAGA_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.apartamento} - {self.bloco}'


