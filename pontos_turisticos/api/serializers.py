from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import PontosTuristicos

class PontoTuristicosSerializer(ModelSerializer):
    class Meta:
        model = PontosTuristicos
        fields = [
            'id','nome','descricao',
        ]

     