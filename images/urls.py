from django.urls import path
from images import views

urlpatterns = [
  path('images/', views.images),
]