from django.urls import path
from submissions import views

urlpatterns = [
  path('contact', views.submit),
]