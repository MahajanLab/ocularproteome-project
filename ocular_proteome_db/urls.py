"""ocular_proteome_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from OcularPDB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # include('OcularPDB.urls')),
    path('home/', views.index, name='index'), #include('OcularPDB.urls')),
    path('search/', views.results, name='index'),
    path('download/', views.download, name='download'),
    path('download_retina/', views.download_retina, name='download_retina'),
    path('download_choroid/', views.download_choroid, name='download_rpe_choroid'),
    path('download_vitreous/', views.download_vitreous, name='download_vitreous'),
    path('download_mouse_vitreous', views.download_mouse_vitrous, name="download_mouse_vitreous"),
    path('download_mouse_retina', views.download_mouse_retina, name="download_mouse_retina")
]
