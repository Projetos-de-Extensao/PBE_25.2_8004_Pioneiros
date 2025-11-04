from django.contrib import admin
from .models import Vaga, Disciplina, Aluno, Inscricao

# Register your models here.
admin.site.register(Vaga)
admin.site.register(Disciplina)
admin.site.register(Aluno)

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'vaga', 'status') # Colunas que ele vê
    list_filter = ('status', 'vaga__unidade', 'vaga__disciplina') # Filtros na lateral
    search_fields = ('aluno__user__username', 'vaga__disciplina__nome') # Barra de busca

    # Ações customizadas (ex: "Aprovar selecionados")
    actions = ['aprovar_inscricoes', 'rejeitar_inscricoes']

    def aprovar_inscricoes(self, request, queryset):
        queryset.update(status='APROVADO')
    aprovar_inscricoes.short_description = "Aprovar inscrições selecionadas"

    def rejeitar_inscricoes(self, request, queryset):
        queryset.update(status='REJEITADO')
    rejeitar_inscricoes.short_description = "Rejeitar inscrições selecionadas"