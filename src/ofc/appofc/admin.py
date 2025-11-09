from django.contrib import admin
from .models import Vaga, Disciplina, Aluno, Inscricao, Curso

# Register your models here.
admin.site.register(Vaga)
admin.site.register(Disciplina)
admin.site.register(Aluno)
admin.site.register(Curso)


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'vaga', 'status') 
    list_filter = ('status', 'vaga__unidade', 'vaga__disciplina') 
    search_fields = ('aluno__user__username', 'vaga__disciplina__nome') 

    actions = ['aprovar_inscricoes', 'rejeitar_inscricoes']

    def aprovar_inscricoes(self, request, queryset):
        queryset.update(status='APROVADO')
    aprovar_inscricoes.short_description = "Aprovar inscrições selecionadas"

    def rejeitar_inscricoes(self, request, queryset):
        queryset.update(status='REJEITADO')
    rejeitar_inscricoes.short_description = "Rejeitar inscrições selecionadas"