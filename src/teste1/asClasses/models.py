from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Base abstrata para usuários
class User(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nome} <{self.email}>"

# Aluno e especializações
class Aluno(User):
    matricula = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def se_candidatar(self, disciplina):
        """
        Método placeholder: cria uma inscrição (Inscricao) do aluno como Candidato.
        Deve ser adaptado conforme fluxo de negócio.
        """
        # implementação de exemplo simplificada (não cria Entrevista)
        candidato, _ = Candidato.objects.get_or_create(
            matricula=self.matricula, defaults={'nome': self.nome, 'email': self.email}
        )
        inscricao = Inscricao.objects.create(disciplina=disciplina)
        inscricao.alunos.add(candidato)
        return inscricao

class Candidato(Aluno):
    status = models.CharField(max_length=50, default='pendente')

    def __str__(self):
        return f"Candidato {self.nome} ({self.status})"

class AlunoMonitorado(Aluno):
    aulas_participadas = models.PositiveIntegerField(default=0)

    def preencher_relatorio_experiencia(self, texto_relatorio):
        # placeholder: salvar/registrar texto de relatório (poderia ser outro modelo)
        # aqui apenas incrementa aulas como exemplo
        # implementar armazenamento real conforme necessidade
        return {"aluno": self.matricula, "relatorio": texto_relatorio}

class Professor(User):
    senha = models.CharField(max_length=128)

    def aprovar_candidato(self, candidato: Candidato):
        candidato.status = 'aprovado'
        candidato.save()
        return candidato

    def ver_relatorio_acompanhamento(self):
        # placeholder: retornar dados de acompanhamento (implementar consulta real)
        return SessaoMonitoria.objects.filter(disciplina__monitor__supervisor=self)

class CASA(User):
    # email herdado de User

    def enviar_informativos_email(self, assunto, corpo, lista_emails):
        # placeholder para integração com serviço de email
        # Real implementation should use Django Email or external provider
        return {"assunto": assunto, "corpo": corpo, "destinatarios": lista_emails}

    def agendar_entrevista(self, entrevista):
        entrevista.agendada_por = self
        entrevista.save()
        return entrevista

# Disciplina e relacionamentos
class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    area = models.CharField(max_length=200, blank=True)
    # opcional: monitor principal (1)
    monitor = models.ForeignKey(
        'TeachingAssistant', null=True, blank=True, on_delete=models.SET_NULL, related_name='monitora_disciplina'
    )

    def __str__(self):
        return self.nome

# TeachingAssistant é especialização de Aluno
class TeachingAssistant(Aluno):
    # relacionamento many-to-many com Disciplinas em que atua
    disciplinas = models.ManyToManyField(Disciplina, related_name='teaching_assistants', blank=True)
    # supervisor (Professor) 0..*
    supervisor = models.ForeignKey(Professor, null=True, blank=True, on_delete=models.SET_NULL, related_name='supervisionados')
    # acompanhada por CASA (0..*)
    acompanhada_por = models.ForeignKey(CASA, null=True, blank=True, on_delete=models.SET_NULL, related_name='tas_acompanhadas')

    def preencher_formulario_frequencias(self, sessao: 'SessaoMonitoria', frequencias: dict):
        """
        Placeholder que registra frequências para uma sessão.
        'frequencias' pode ser um dict {aluno_id: presença_bool} — adaptar conforme necessidade.
        """
        # implementar lógica de registro das frequências
        return {"sessao": sessao.id if sessao else None, "frequencias_recebidas": frequencias}

# Inscrição - um relacionamento entre candidatos e disciplina
class Inscricao(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='inscricoes')
    alunos = models.ManyToManyField(Candidato, related_name='inscricoes', blank=True)
    # 0..1 entrevista gerada a partir da inscrição
    entrevista = models.OneToOneField('Entrevista', null=True, blank=True, on_delete=models.SET_NULL, related_name='inscricao')

    def __str__(self):
        return f"Inscricao em {self.disciplina.nome}"

# Entrevista envolvendo candidatos, professores e possivelmente agendada por CASA
class Entrevista(models.Model):
    candidatos = models.ManyToManyField(Candidato, related_name='entrevistas')
    professores = models.ManyToManyField(Professor, related_name='entrevistas')
    agendada_por = models.ForeignKey(CASA, null=True, blank=True, on_delete=models.SET_NULL, related_name='entrevistas_agendadas')
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Entrevista {self.id} - {self.data.isoformat()}"

# Sessão de monitoria
class SessaoMonitoria(models.Model):
    data = models.DateField(default=timezone.now)
    monitorados = models.ManyToManyField(AlunoMonitorado, related_name='sessoes', blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='sessoes')

    @property
    def qtd_alunos(self):
        return self.monitorados.count()

    def __str__(self):
        return f"Sessao de {self.disciplina.nome} em {self.data.isoformat()}"