from django.contrib import admin
from generator.models import Trecho


class TrechoAdmin(admin.ModelAdmin):
    fields = ('text', 'coluna')
    list_display = ('text', 'coluna')
    list_filter = ('coluna',)

admin.site.register(Trecho, TrechoAdmin)