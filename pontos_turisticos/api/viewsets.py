from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontosTuristicos
from .serializers import PontoTuristicosSerializer

class PontosTuristicosViewSet(ModelViewSet):
    
    queryset = PontosTuristicos.objects.all()
    serializer_class = PontoTuristicosSerializer

