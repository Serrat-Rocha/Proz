from django.db import models
from django.contrib.auth.models import User

class Estoque(models.Model):
    produto = models.CharField(max_length=200)
    quantidade_disponivel = models.IntegerField(default=0)
    valor_unitario = models.FloatField(default=0)
    categoria = models.CharField(max_length=100, default="Geral")  # novo
    validade = models.DateField(null=True, blank=True)             # novo
    raridade = models.CharField(
        max_length=50,
        choices=[
            ('E', 'E'),
            ('C', 'C'),
            ('B', 'B'),
            ('A', 'A'),
            ('S', 'S')
        ],
        default='comum'
    )  # novo

    def __str__(self):
        return self.produto


    def __str__(self):
        return self.produto

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'Perfil de {self.user.username}'