from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from altotech.users.api.views import UserViewSet
from produtos.api.views import EnderecoViewSet, ClienteViewSet, ItemViewSet, EstoqueViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("endereco", EnderecoViewSet, basename="endereco")
router.register("clientes", ClienteViewSet, basename="clientes")
router.register("itens", ItemViewSet, basename="itens")
router.register("estoque", EstoqueViewSet, basename="estoque")


app_name = "api"
urlpatterns = router.urls
