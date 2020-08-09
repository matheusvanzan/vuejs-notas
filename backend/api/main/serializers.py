from rest_framework import serializers
from main.models import Nota

class NotaSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Nota
        fields = ['id', 'titulo', 'conteudo', 'ativa']