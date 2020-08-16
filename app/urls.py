from django.contrib import admin
from django.urls import path, include
from .views import index, customer_entry

urlpatterns = [
    path('',customer_entry, name = "index"),
]