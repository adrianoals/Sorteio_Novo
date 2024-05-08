from django.db import models

class ApartamentoTorre1(models.Model):
    numero_apartamento = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.numero_apartamento}"


class VagaTorre1(models.Model):
    vaga = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.vaga


class SorteioTorre1(models.Model):
    apartamento = models.OneToOneField(ApartamentoTorre1, on_delete=models.CASCADE)
    vaga = models.OneToOneField(VagaTorre1, on_delete=models.CASCADE)

    def __str__(self):
        # Acesso ao bloco através do apartamento
        return f"Apartamento {self.apartamento.numero_apartamento}  Vaga: {self.vaga.vaga}"

