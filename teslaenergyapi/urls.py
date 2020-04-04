"""teslaenergyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/v1/', include('eventos.urls')),
    url(r'^api/v1/usuarios/', include('users.urls')),
    url(r'^api/v1/clientes/', include('clients.urls')),
    url(r'^api/v1/assets/', include('assets.urls')),
    #url(r'^api/v1/imagenes/', include('imagenes.urls')),
    url(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/auth-jwt/', obtain_jwt_token),
    url(r'^api/v1/auth-jwt-refresh/', refresh_jwt_token),
    url(r'^api/v1/auth-jwt-verify/', verify_jwt_token),

]
