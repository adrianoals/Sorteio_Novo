from django.db import models

class Bloco(models.Model):

    BLOCO_CHOICES = [
        ('A', 'A',),
        ('B', 'B',),
    ]
    bloco = models.CharField(max_length=100, unique=True, choices=BLOCO_CHOICES)

    def __str__(self):
        return self.bloco

class Apartamento(models.Model):
    
    APARTAMENTO_CHOICES = [
        ('Apto 01', 'Apto 01'),
        ('Apto 02', 'Apto 02'),
        ('Apto 11', 'Apto 11'),
        ('Apto 12', 'Apto 12'),
        ('Apto 13', 'Apto 13'),
        ('Apto 14', 'Apto 14'),
        ('Apto 15', 'Apto 15'),    
        ('Apto 16', 'Apto 16'),    
        ('Apto 21', 'Apto 21'),
        ('Apto 22', 'Apto 22'),
        ('Apto 23', 'Apto 23'),
        ('Apto 24', 'Apto 24'),
        ('Apto 25', 'Apto 25'),    
        ('Apto 26', 'Apto 26'),    
        ('Apto 31', 'Apto 31'),
        ('Apto 32', 'Apto 32'),
        ('Apto 33', 'Apto 33'),
        ('Apto 34', 'Apto 34'),
        ('Apto 35', 'Apto 35'),    
        ('Apto 36', 'Apto 36'),    
        ('Apto 41', 'Apto 41'),
        ('Apto 42', 'Apto 42'),
        ('Apto 43', 'Apto 43'),
        ('Apto 44', 'Apto 44'),
        ('Apto 45', 'Apto 45'),    
        ('Apto 46', 'Apto 46'),    
    ]

    numero_apartamento = models.CharField(max_length=50, choices=APARTAMENTO_CHOICES)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('numero_apartamento', 'bloco',)  # Garante a unicidade da combinação

    def __str__(self):
        return f"{self.numero_apartamento} - Bloco {self.bloco.bloco}"


class Vaga(models.Model):

    VAGA_CHOICES = [
        ('Vaga 01 Bloco B', 'Vaga 01 Bloco B'),
        ('Vaga 02 Bloco B', 'Vaga 02 Bloco B'),
        ('Vaga 03 Bloco B', 'Vaga 03 Bloco B'),
        ('Vaga 04 Bloco B', 'Vaga 04 Bloco B'),
        ('Vaga 05 Bloco B', 'Vaga 05 Bloco B'), 
        ('Vaga 06 Bloco B', 'Vaga 06 Bloco B'), 
        ('Vaga 07 Bloco B', 'Vaga 07 Bloco B'), 
        ('Vaga 08 Bloco B', 'Vaga 08 Bloco B'), 
        ('Vaga 09 Bloco B', 'Vaga 09 Bloco B'), 
        ('Vaga 10 Bloco B', 'Vaga 10 Bloco B'), 
        ('Vaga 11 Bloco B', 'Vaga 11 Bloco B'), 
        ('Vaga 12 Bloco B', 'Vaga 12 Bloco B'), 
        ('Vaga 13 Bloco B', 'Vaga 13 Bloco B'), 
        ('Vaga 14 Bloco B', 'Vaga 14 Bloco B'), 
        ('Vaga 15 Bloco B', 'Vaga 15 Bloco B'), 
        ('Vaga 16 Bloco B', 'Vaga 16 Bloco B'), 
        ('Vaga 17 Bloco B', 'Vaga 17 Bloco B'), 
        ('Vaga 18 Bloco B', 'Vaga 18 Bloco B'), 
        ('Vaga 19 Bloco B', 'Vaga 19 Bloco B'), 
        ('Vaga 20 Bloco B', 'Vaga 20 Bloco B'), 
        ('Vaga 21 Bloco B', 'Vaga 21 Bloco B'), 
        ('Vaga 22 Bloco B', 'Vaga 22 Bloco B'), 
        ('Vaga 23 Bloco B', 'Vaga 23 Bloco B'), 
        ('Vaga 24 Bloco B', 'Vaga 24 Bloco B'), 
        ('Vaga 25 Bloco B', 'Vaga 25 Bloco B'), 
        ('Vaga 26 Bloco B', 'Vaga 26 Bloco B'), 
        ('Vaga 27 Bloco A', 'Vaga 27 Bloco A'), 
        ('Vaga 28 Bloco A', 'Vaga 28 Bloco A'), 
        ('Vaga 29 Bloco A', 'Vaga 29 Bloco A'), 
        ('Vaga 30 Bloco A', 'Vaga 30 Bloco A'), 
        ('Vaga 31 Bloco A', 'Vaga 31 Bloco A'), 
        ('Vaga 32 Bloco A', 'Vaga 32 Bloco A'), 
        ('Vaga 33 Bloco A', 'Vaga 33 Bloco A'), 
        ('Vaga 34 Bloco A', 'Vaga 34 Bloco A'), 
        ('Vaga 35 Bloco A', 'Vaga 35 Bloco A'), 
        ('Vaga 36 Bloco A', 'Vaga 36 Bloco A'),
        ('Vaga 37 Bloco A', 'Vaga 37 Bloco A'),
        ('Vaga 38 Bloco A', 'Vaga 38 Bloco A'),
        ('Vaga 39 Bloco A', 'Vaga 39 Bloco A'),
        ('Vaga 40 Bloco A', 'Vaga 40 Bloco A'),
        ('Vaga 41 Bloco A', 'Vaga 41 Bloco A'),
        ('Vaga 42 Bloco A', 'Vaga 42 Bloco A'),
        ('Vaga 43 Bloco A', 'Vaga 43 Bloco A'),
        ('Vaga 44 Bloco A', 'Vaga 44 Bloco A'),
        ('Vaga 45 Bloco A', 'Vaga 45 Bloco A'),
        ('Vaga 46 Bloco A', 'Vaga 46 Bloco A'),
        ('Vaga 47 Bloco A', 'Vaga 47 Bloco A'),
        ('Vaga 48 Bloco A', 'Vaga 48 Bloco A'),
        ('Vaga 49 Bloco A', 'Vaga 49 Bloco A'),
        ('Vaga 50 Bloco A', 'Vaga 50 Bloco A'),	

    ]

    vaga = models.CharField(max_length=50, unique=True, choices=VAGA_CHOICES)

    def __str__(self):
        return self.vaga


class Sorteio(models.Model):
    apartamento = models.OneToOneField(Apartamento, on_delete=models.CASCADE)
    vaga = models.OneToOneField(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        # Acesso ao bloco através do apartamento
        return f"Apartamento {self.apartamento.numero_apartamento} - Bloco {self.apartamento.bloco.bloco} - Vaga {self.vaga.vaga}"
