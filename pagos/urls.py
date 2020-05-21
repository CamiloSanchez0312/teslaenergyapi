from django.conf.urls import url
from .api import PagoApi, PagoListApi

urlpatterns = [
    url(r'^$', PagoListApi.as_view()),
    url(r'^create/$', PagoApi.as_view()),
]