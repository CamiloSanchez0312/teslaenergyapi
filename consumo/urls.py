from django.conf.urls import url
from .api import ConsumoApi, FacturaApi, FacturaApiList

urlpatterns = [
    url(r'^consumo/create/$', ConsumoApi.as_view()),
    url(r'^factura/create/$', FacturaApi.as_view()),
    url(r'^factura/$', FacturaApiList.as_view()),
]
