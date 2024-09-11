from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    data_evento = models.DateTimeField()
    capacidade = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo


class Paticipante(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
