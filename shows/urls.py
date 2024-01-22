from django.urls import path
from shows import views

urlpatterns = [
  path('shows/', views.shows),
  path('past_shows/', views.past_shows),
]
