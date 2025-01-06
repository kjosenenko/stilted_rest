from django.urls import path
from social_media import views

urlpatterns = [
  path('social_media/', views.social_media),
]