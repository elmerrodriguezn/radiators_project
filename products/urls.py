from django.urls import path
from . import views

urlpatterns = [
    path('<str:default_code>/', views.single, name='single'),
    path('busqueda', views.search, name='busqueda'),
    path('iniciativa', views.lead, name='lead')
]