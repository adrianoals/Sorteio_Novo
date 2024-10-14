from django.db import models

# Representa cada apartamento
class Apartamento(models.Model):
    numero = models.CharField(max_length=5)  # Ex: "1404", "1501"
    andar = models.IntegerField()  # Ex: "14", "15", "16"
    direito_vaga_dupla = models.BooleanField(default=False)
    direito_duas_vagas_livres = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Apartamento {self.numero}"

# Representa as vagas de garagem, incluindo simples e duplas
class Vaga(models.Model):
    SUBSOLO_CHOICES = [
        ('1SS', '1º Subsolo'),
        ('2SS', '2º Subsolo'),
        ('3SS', '3º Subsolo'),
        ('4SS', '4º Subsolo')
    ]
    
    numero = models.CharField(max_length=5)  # Ex: "Vaga 01", "Vaga 02"
    subsolo = models.CharField(max_length=3, choices=SUBSOLO_CHOICES)
    tipo_vaga = models.CharField(max_length=10, choices=[('simples', 'Simples'), ('dupla', 'Dupla')])
    dupla_com = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)  # Para vagas duplas, indica com qual vaga está pareada
    
    def __str__(self):
        return f"{self.numero} - {self.subsolo}"

# Armazena o resultado do sorteio, vinculando apartamentos a vagas
class Sorteio(models.Model):
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data_sorteio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Sorteio: {self.apartamento} -> {self.vaga}"

