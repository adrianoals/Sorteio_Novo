from django.db import models

class Apartamento(models.Model):    
    numero_apartamento = models.CharField(max_length=50)
    pcd = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.numero_apartamento}"


class Vaga(models.Model):
    vaga = models.CharField(max_length=50, unique=True)
    coberta = models.BooleanField(default=False)
    pcd = models.BooleanField(default=False)

    def __str__(self):
        return self.vaga


class Sorteio(models.Model):
    apartamento = models.OneToOneField(Apartamento, on_delete=models.CASCADE)
    vaga = models.OneToOneField(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        # Acesso ao bloco através do apartamento
        return f"Apartamento {self.apartamento.numero_apartamento}  Vaga: {self.vaga.vaga}"


class ApartamentoMoto(models.Model):    
    numero_apartamento = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.numero_apartamento}"


class VagaMoto(models.Model):
    vaga = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.vaga


class SorteioMoto(models.Model):
    apartamento = models.OneToOneField(ApartamentoMoto, on_delete=models.CASCADE)
    vaga = models.OneToOneField(VagaMoto, on_delete=models.CASCADE)

    def __str__(self):
        # Acesso ao bloco através do apartamento
        return f"Apartamento {self.apartamento.numero_apartamento}  Vaga: {self.vaga.vaga}"
