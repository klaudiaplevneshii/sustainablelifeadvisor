from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('calculate/', views.calculate, name='calculate'),
    path('about/', views.about_view, name='about'),
    path('history/', views.view_history, name='view_history'),
    path('delete_history/', views.clear_history, name='delete_history'),
    path('impact/', views.impact_view, name='impact'),
    path('interpretation/', views.interpretation_view, name='interpretation'),
    path('result/db/<int:record_id>/', views.result_from_db_history, name='result_from_db_history'),
]

