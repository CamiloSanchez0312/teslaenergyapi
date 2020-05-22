from django.conf.urls import url
from .api import ClienteRegisterAPI, ClienteListAPI, ClienteByCedulaAPI

urlpatterns = [
    url(r'^$', ClienteListAPI.as_view()),
    url(r'^create/$', ClienteRegisterAPI.as_view()),
    url(r'^bycedula/(?P<id>[1-9]+)/$', ClienteByCedulaAPI.as_view()),
]
