from django.conf.urls import url
from .api import UserAPI, UserByIdAPI, UserByUsernameAPI, RegisterAPI, VerifyTokenAPI

urlpatterns = [
    url(r'^$', UserAPI.as_view()),
    url(r'^create/$', RegisterAPI.as_view(), name = 'usuario-api-create'),
    url(r'^byid/(?P<pk>[0-9]+)/$', UserByIdAPI.as_view(), name = 'usuario-pk-api'),
    url(r'^byusername/(?P<username>[a-z1-9A-Z]+)/$', UserByUsernameAPI.as_view(), name = 'usuario-username-api'),
    url(r'^verifyrecaptcha/', VerifyTokenAPI.as_view()),
]
