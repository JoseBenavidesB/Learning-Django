"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainapp.urls")),
    path('', include("pages.urls")),
    path('', include("blog.urls")),
]


#esta configuración es para tener disponible una url para cada imagen que se suba

#ruta imagenes
if settings.DEBUG: #esto para poder cargar las imagenes en el servidor local
    from django.conf.urls.static import static #se usa esta de cargar cosas estaticas del framework para cargar los ficheros imagenes
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)