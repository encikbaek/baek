from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('<int:product_id>', views.product, name='products'),
    path('search', views.search, name='search'),
]