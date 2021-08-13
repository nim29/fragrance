from django.urls import path
from . import views

urlpatterns = [
    path('perfumes/', views.perfumes),
]