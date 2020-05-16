from django.conf.urls import url
from .api import SubstationRegisterAPI, SubstationListAPI, TransformerRegisterAPI, TransformerListAPI, ElectricMeterRegisterAPI, ElectricMeterListAPI, SubstationByIdAPI, TransformerByIdAPI, ElectricMeterByIdAPI, MedicionesApi

urlpatterns = [
    url(r'^substation/$', SubstationListAPI.as_view()),
    url(r'^substation/byid/(?P<pk>[0-9]+)/$', SubstationByIdAPI.as_view()),
    url(r'^substation/create/$', SubstationRegisterAPI.as_view()),
    url(r'^transformer/$', TransformerListAPI.as_view()),
    url(r'^transformer/byid/(?P<pk>[0-9]+)/$', TransformerByIdAPI.as_view()),
    url(r'^transformer/create/$', TransformerRegisterAPI.as_view()),
    url(r'^electricmeter/$', ElectricMeterListAPI.as_view()),
    url(r'^electricmeter/byid/(?P<pk>[0-9]+)/$', ElectricMeterByIdAPI.as_view()),
    url(r'^electricmeter/create/$', ElectricMeterRegisterAPI.as_view()),
    url(r'^mediciones/create/$', MedicionesApi.as_view()),
]
