from django.db import models

# Representa cada apartamento participante
class Apartamento(models.Model):
    numero = models.CharField(max_length=10)  # Exemplo: "405", "101"
    is_pne = models.BooleanField(default=False)  # Indica se o apartamento é elegível para vaga PNE
    is_idoso = models.BooleanField(default=False)  # Indica se o apartamento é elegível para vaga de Idoso

    def __str__(self):
        return f"Apartamento {self.numero}"

# Representa cada vaga de estacionamento
class Vaga(models.Model):
    TIPO_VAGA_CHOICES = [
        ('DUPLA', 'Vaga Dupla'),
        ('LIVRE', 'Vaga Livre'),
    ]
    ESPECIAL_VAGA_CHOICES = [
        ('NORMAL', 'Normal'),
        ('PNE', 'PNE'),
        ('IDOSO', 'Idoso'),
    ]
    numero = models.CharField(max_length=5)  # Exemplo: "01", "07-08" para vagas duplas
    tipo = models.CharField(max_length=6, choices=TIPO_VAGA_CHOICES)  # Tipo da vaga: Dupla ou Livre
    especial = models.CharField(max_length=6, choices=ESPECIAL_VAGA_CHOICES, default='NORMAL')  # Classificação especial
    subsolo = models.IntegerField(choices=[(1, 'Subsolo 1'), (2, 'Subsolo 2')])  # Subsolo da vaga
    is_livre_quando_nao_especial = models.BooleanField(default=True)  # Se a vaga especial pode ser sorteada como vaga livre

    # Para vagas duplas, indicamos a segunda vaga que faz par com a primeira
    dupla_com = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='dupla')

    def __str__(self):
        return f"Vaga {self.numero} ({self.get_tipo_display()}, {self.get_especial_display()})"

# Registra o resultado de um sorteio entre um apartamento e uma vaga
class Sorteio(models.Model):
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data_sorteio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.apartamento.numero} -> {self.vaga.numero} em {self.data_sorteio}"

# Model para representar a dupla de apartamentos (pré-formadas para sorteio de vagas duplas)
class DuplaApartamentos(models.Model):
    apartamento_1 = models.ForeignKey(Apartamento, on_delete=models.CASCADE, related_name='dupla_apartamento_pre_1')
    apartamento_2 = models.ForeignKey(Apartamento, on_delete=models.CASCADE, related_name='dupla_apartamento_pre_2', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dupla: {self.apartamento_1} e {self.apartamento_2}"

class SorteioDupla(models.Model):
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data_sorteio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.apartamento.numero} -> Vaga {self.vaga.numero} (Dupla com {self.vaga.dupla_com.numero if self.vaga.dupla_com else 'N/A'}) em {self.data_sorteio}"

