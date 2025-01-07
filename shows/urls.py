from django.urls import path
from shows import views

urlpatterns = [
  path('shows/', views.shows),
  path('show/<int:id>', views.show),
]
