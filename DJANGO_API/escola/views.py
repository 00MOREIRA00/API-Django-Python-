from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    # Query que será utilizada na busca
    queryset = Aluno.objects.all()

    # Class serializer que será responsavel pela conversão
    serializer_class = AlunoSerializer 