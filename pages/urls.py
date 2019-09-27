from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_sneakers, name='add_sneakers'),
    path('details/<int:pk>/', views.sneakers_details, name='sneakers_details')
]
