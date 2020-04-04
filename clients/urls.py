from django.conf.urls import url 
from users import views
from .api import ClienteRegisterAPI,ClienteListAPI,ClienteByCedulaAPI

urlpatterns = [
    url(r'^cliente/create/$',ClienteRegisterAPI.as_view()),
    url(r'^cliente/$',ClienteListAPI.as_view()),
    url(r'^cliente/bycedula/(?P<cedula>[1-9]+)/$',ClienteByCedulaAPI.as_view()),
]
