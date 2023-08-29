from rest_framework.serializers import ModelSerializer
from produtos.models import Endereco, Cliente, Item, Estoque

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class EstoqueSerializer(ModelSerializer):
    class Meta:
        model = Estoque
        fields = "__all__"
