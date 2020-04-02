from django.conf.urls import url 
from users import views
from .api import UserAPI,UserByIdAPI,UserByUsernameAPI,RegisterAPI
from .viewsets import UsuarioViewSetsUsername,UsuariosAll

urlpatterns = [
    url(r'^$', UserAPI.as_view()),
    url(r'^byid/(?P<pk>[0-9]+)/$', UserByIdAPI.as_view(), name = 'usuario-pk-api'),
    url(r'^byusername/(?P<username>[a-z1-9]+)/$', UserByUsernameAPI.as_view(), name = 'usuario-username-api'),
    url(r'^create/$', RegisterAPI.as_view(), name = 'usuario-api-create'),
]
