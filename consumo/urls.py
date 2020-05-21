from django.conf.urls import url
from .api import ConsumoApi, FacturaApi, FacturaApiList, FacturaApiID

urlpatterns = [
    url(r'^consumo/create/$', ConsumoApi.as_view()),
    url(r'^factura/create/$', FacturaApi.as_view()),
    url(r'^factura/$', FacturaApiList.as_view()),
    url(r'^facturabyid/(?P<pk>[0-9]+)/$', FacturaApiID.as_view())
]
