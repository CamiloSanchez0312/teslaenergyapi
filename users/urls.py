from django.conf.urls import url 
from users import views
from .api import UserAPI,UserByIdAPI,UserByUsernameAPI
from .viewsets import UsuarioViewSetsUsername,UsuariosAll
'''
router = routers.SimpleRouter()
router.register(r'byUsername',UsuarioViewSetsUsername,basename='usuario-api-lista')
router.register(r'',UsuariosAll,basename='usuario-api-all')

'''
urlpatterns = [
    url(r'^$', UserAPI.as_view()),
    url(r'^byid/(?P<pk>[0-9]+)/$', UserByIdAPI.as_view(), name = 'usuario-pk-api'),
    url(r'^byusername/(?P<username>[a-z1-9]+)/$', UserByUsernameAPI.as_view(), name = 'usuario-username-api'),
    url(r'^nuevo/$', views.UsuarioCreateApi.as_view(), name = 'usuario-api-create'),
]

#urlpatterns = router.urls 
