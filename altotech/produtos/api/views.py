from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from produtos.api.serializers import EnderecoSerializer, ClienteSerializer, ItemSerializer, EstoqueSerializer
from produtos.models import Endereco, Cliente, Item, Estoque
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class EnderecoViewSet(ModelViewSet):
    serializer_class = EnderecoSerializer
    permission_classes = [ AllowAny ]
    queryset = Endereco.objects.all()

class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [ AllowAny ]
    queryset = Cliente.objects.all()

class ItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [ AllowAny ]
    queryset = Item.objects.all()

    @action(methods=['post'],detail=False, url_path="venda")
    def vender_item(self, request):
        data = request.data
        codigo = data['codigo_item']
        nome = data['nome_item']
        descricao = data['descricao_item']
        valor = data['valor_item']
        quantidade = data['quantidade_item']

        item = Item.objects.create(
            codigo = codigo,
            nome = nome,
            descricao = descricao,
            valor = valor,
            quantidade = quantidade,
        )
        item.save()

        serializer = ItemSerializer(item)
        return Response({"mensagem" : "Compra realizada com sucesso", "data": serializer.data}, status=status.HTTP_200_OK)

class EstoqueViewSet(ModelViewSet):
    serializer_class = EstoqueSerializer
    permission_classes = [ AllowAny ]
    queryset = Estoque.objects.all()