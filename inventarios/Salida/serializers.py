from rest_framework import serializers
from .models import Salida
from Insumo.serializers import InsumoSerializer
from Entrada.models import Entrada

class SalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salida
        fields = ('fecha_salida','insumo','cantidad','valor_total_salida')
        extra_kwargs = {
            'entradas': {'required': False}
        }
