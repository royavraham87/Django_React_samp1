from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
path('',views.index),
path('products',views.Products),
path('addproduct',views.addproduct),
path('delproduct/<int:id>',views.delproduct),
]
