from django.contrib import admin
from produtos.models import Endereco, Item, Estoque, Cliente

# Register your models here.
admin.site.register(Endereco)
admin.site.register(Item)
admin.site.register(Estoque)
admin.site.register(Cliente)