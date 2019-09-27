from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_sneakers, name='add_sneakers'),
    path('details/<int:pk>/', views.sneakers_details, name='sneakers_details'),
    path('delete/<int:pk>/', views.delete_sneakers, name='delete_sneakers'),
    path('edit/<int:pk>/', views.edit_sneakers, name='edit_sneakers'),
]
