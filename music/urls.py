from django.urls import path
from music import views

urlpatterns = [
  path('api/music/', views.music),
]