from app.models import Cadastro

from rest_framework import serializers

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['id', 'name', 'cpf', 'created_at']