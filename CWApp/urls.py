from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('gallery/', views.gallery, name='gallery'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('resources/', views.resources, name='resources'),
]
