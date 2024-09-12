from django.contrib import admin
from .models import Evento, Paticipante


class Eventos(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "local",
        "data_evento",
        "capacidade",
    )
    list_display_links = (
        "id",
        "titulo",
    )
    list_per_page = 20
    search_fields = (
        "titulo",
        "local",
    )


admin.site.register(Evento, Eventos)


class Participantes(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "cpf",
        "email",
        "telefone",
    )
    list_display_links = (
        "id",
        "nome",
    )
    list_per_page = 20
    search_fields = (
        "nome",
        "email",
    )

admin.site.register(Paticipante, Participantes)
