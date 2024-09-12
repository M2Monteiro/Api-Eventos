from rest_framework import viewsets
from .models import Evento, Paticipante
from .serializers import EventoSerializer, ParticipanteSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Paticipante.objects.all()
    serializer_class = ParticipanteSerializer
