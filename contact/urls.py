from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead, name='lead'),
]


