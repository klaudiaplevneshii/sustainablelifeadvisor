"""
URL configuration for carbon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views
from landing.views import view_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('calculate/', views.calculate, name='calculate'),
    path('result/', views.result, name='result'),
    path('about/', views.about_view, name='about'),
    path('history/', views.view_history, name='view_history'),

    path('delete_history/', views.clear_history, name='delete_history'),

    path('impact/', views.impact_view, name='impact'),

]
