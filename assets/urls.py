from django.conf.urls import url
from .api import SubstationRegisterAPI, SubstationListAPI

urlpatterns = [
    url(r'^substation/create/$', SubstationRegisterAPI.as_view()),
    url(r'^substation/$', SubstationListAPI.as_view()),
]
