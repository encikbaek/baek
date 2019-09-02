from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='clients'),
    path('creates', views.creates, name='creates'),
    path('access', views.access, name='access'),
]