from rest_framework import viewsets, generics, mixins, status
from rest_framework.response import Response
from .models import Vaga, Disciplina, Inscricao
from .serializers import VagaSerializer, DisciplinaSerializar, InscricaoSerializer, CadastroAlunoSerializer, InscricaoCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(
        description="Lista todos os conteúdos públicos",
        tags=["Content"]
    ),
    create=extend_schema(
        description="Cria um novo conteúdo (requer autenticação)",
        tags=["Content"]
    ),
    retrieve=extend_schema(
        description="Obtém detalhes de um conteúdo específico",
        tags=["Content"]
    ),
    update=extend_schema(
        description="Atualiza um conteúdo existente (apenas o criador)",
        tags=["Content"]
    ),
    destroy=extend_schema(
        description="Remove um conteúdo (apenas o criador)",
        tags=["Content"]
    ),
)

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializar
    permission_classes = [IsAuthenticated]

class VagaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VagaSerializer

    def get_queryset(self):
        queryset = Vaga.objects.all()

        curso = self.request.query_params.get('curso')

        if curso:
            queryset = queryset.filter(disciplina__curso__icontains=curso)
        
        return queryset.order_by('disciplina__nome')
    
    

class InscricaoViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'aluno'):
            return Inscricao.objects.filter(aluno=self.request.user.aluno).prefetch_related('vaga__disciplina')
        return Inscricao.objects.none()

    def get_serializer_class(self):

        if self.action == 'create':
            return InscricaoCreateSerializer 
        
        return InscricaoSerializer
    
    def get_serializer_context(self):
        return {'request': self.request, 'format': self.format_kwarg, 'view': self}

class CadastroAlunoView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    
    serializer_class = CadastroAlunoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Aluno cadastro com sucesso!"}, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )


