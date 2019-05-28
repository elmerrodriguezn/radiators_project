from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('send_lead/', views.send_lead, name='send_lead')
]


