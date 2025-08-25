from django.db import models
from django.utils import timezone

class Turno(models.Model):
    TIPO_CLIENTE = [
        ('N', 'Normal'),
        ('E', 'Embarazada'),
        ('T', 'Tercera Edad'),
    ]
    numero = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=TIPO_CLIENTE)
    hora_creacion = models.DateTimeField(default=timezone.now)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.numero}"
