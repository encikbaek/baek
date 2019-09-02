from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', include('product.urls')),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]