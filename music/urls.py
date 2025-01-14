from django.urls import path
from music import views

urlpatterns = [
    path('music/', views.music),  # Remove duplicate 'api' prefix
]