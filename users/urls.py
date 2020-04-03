from django.conf.urls import url 
from users import views
from .api import UserAPI,UserByIdAPI,UserByUsernameAPI,RegisterAPI,ClienteRegisterAPI,ClienteListAPI,ClienteByCedulaAPI
from .viewsets import UsuarioViewSetsUsername,UsuariosAll

urlpatterns = [
    url(r'^$', UserAPI.as_view()),
    url(r'^byid/(?P<pk>[0-9]+)/$', UserByIdAPI.as_view(), name = 'usuario-pk-api'),
    url(r'^byusername/(?P<username>[a-z1-9A-Z]+)/$', UserByUsernameAPI.as_view(), name = 'usuario-username-api'),
    url(r'^create/$', RegisterAPI.as_view(), name = 'usuario-api-create'),
    url(r'^cliente/create/$',ClienteRegisterAPI.as_view()),
    url(r'^cliente/$',ClienteListAPI.as_view()),
    url(r'^cliente/bycedula/(?P<cedula>[1-9]+)/$',ClienteByCedulaAPI.as_view()),
]
