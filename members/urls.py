from django.urls import path
from members import views

urlpatterns = [
  path('band_members/', views.band_members),
]