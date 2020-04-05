from django.conf.urls import url
from .api import SubstationRegisterAPI, SubstationListAPI, TransformerRegisterAPI, TransformerListAPI, ElectricMeterRegisterAPI, ElectricMeterListAPI

urlpatterns = [
    url(r'^substation/$', SubstationListAPI.as_view()),
    url(r'^substation/create/$', SubstationRegisterAPI.as_view()),
    url(r'^transformer/$', TransformerListAPI.as_view()),
    url(r'^transformer/create/$', TransformerRegisterAPI.as_view()),
    url(r'^electricmeter/$', ElectricMeterListAPI.as_view()),
    url(r'^electricmeter/create/$', ElectricMeterRegisterAPI.as_view()),
]
