from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products.index'),
    path('<str:default_code>/', views.single, name='single'),
    path('search', views.search, name='search'),
    path('product_lead', views.lead, name='product_lead'),
]