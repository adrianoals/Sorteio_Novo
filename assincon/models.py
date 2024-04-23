from django.db import models

class ListaSindicos(models.Model):
    nome = models.CharField(max_length=150,)
    def __str__(self):
        return f'{self.nome}'

class Sorteio(models.Model):
    sindico = models.ForeignKey('ListaSindicos', on_delete=models.CASCADE)
    sorteado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sindico.nome} - {'Sorteado' if self.sorteado else 'Não Sorteado'}"
    

    