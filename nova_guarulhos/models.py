from django.db import models

class Apartamento(models.Model):
    bloco = models.CharField(max_length=50, default='Bloco 01')
    numero_apartamento = models.CharField(max_length=50)
    pcd = models.BooleanField(default=False) 
    idoso = models.BooleanField(default=False) 
    adimplentes = models.BooleanField(default=False) 
    presenca = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.numero_apartamento}"


class Vaga(models.Model):
    vaga = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.vaga


class Sorteio(models.Model):
    apartamento = models.OneToOneField(Apartamento, on_delete=models.CASCADE)
    vaga = models.OneToOneField(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        # Acesso ao bloco através do apartamento
        return f"Bloco {self.apartamento.bloco} - Apartamento {self.apartamento.numero_apartamento}  Vaga: {self.vaga.vaga}"
