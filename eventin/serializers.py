from rest_framework import serializers
from .models import Evento, Paticipante


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ["id", "titulo", "descricao", "local", "data_evento", "capacidade"]


class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paticipante
        fields = ["id", "nome", "cpf", "email", "telefone"]
