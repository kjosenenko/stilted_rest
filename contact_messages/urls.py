from django.urls import path
from contact_messages import views

urlpatterns = [
  path('contact/', views.contact),
]