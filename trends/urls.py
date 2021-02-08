from django.urls import path

from . import views

urlpatterns = [
    path('hits/', views.reddit, name='reddit'),
    path('ihub/', views.ihub, name='ihub'),
]