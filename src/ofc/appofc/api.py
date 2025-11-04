from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from .models import Vaga, Disciplina, Inscricao
from .serializers import VagaSerializer, DisciplinaSerializar, InscricaoSerializer, CadastroAlunoSerializer, InscricaoCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializar
    permission_classes = [IsAuthenticated]

class VagaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vaga.objects.all() 
    serializer_class = VagaSerializer 
    permission_classes = [IsAuthenticated]

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