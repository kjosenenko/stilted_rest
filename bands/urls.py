from django.urls import path
from bands import views

urlpatterns = [
  path('band/', views.band),
  path('band/images', views.images),
]
