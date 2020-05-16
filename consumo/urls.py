from django.conf.urls import url
from .api import ConsumoApi, FacturaApi

urlpatterns = [
    url(r'^consumo/create/$', ConsumoApi.as_view()),
    url(r'^factura/create/$', FacturaApi.as_view()),
]
