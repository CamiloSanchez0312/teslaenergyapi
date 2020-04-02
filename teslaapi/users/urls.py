from django.conf.urls import url 
from users import views
from .api import UserAPI,UserByIdAPI,UserByUsernameAPI,RegisterAPI
from .viewsets import UsuarioViewSetsUsername,UsuariosAll
from .views import usuario_view
'''
router = routers.SimpleRouter()
router.register(r'byUsername',UsuarioViewSetsUsername,basename='usuario-api-lista')
router.register(r'',UsuariosAll,basename='usuario-api-all')

'''
urlpatterns = [
    url(r'^$', UserAPI.as_view()),
    url(r'^create$', usuario_view, name = "Create"),
    url(r'^byid/(?P<pk>[0-9]+)/$', UserByIdAPI.as_view(), name = 'usuario-pk-api'),
    url(r'^byusername/(?P<username>[a-z1-9]+)/$', UserByUsernameAPI.as_view(), name = 'usuario-username-api'),
    url(r'^create/$', RegisterAPI.as_view(), name = 'usuario-api-create'),
]

#urlpatterns = router.urls 
