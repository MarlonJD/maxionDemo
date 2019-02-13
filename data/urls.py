from django.urls import path
from . import views

# app_name = 'notes'
urlpatterns = [
    # Index Page
    path('', views.index, name='index'),
    path('createData/', views.createData, name='createData'),
    path('data/<uuid:uuid>/', views.dataView, name='dataView'),
    path('delete/<uuid:uuid>/', views.delete, name='delete'),
    path('deleteAll/', views.deleteAll, name='deleteAll'),
    path('makeDefault/<uuid:uuid>/', views.makeDefault, name='makeDefault'),
]