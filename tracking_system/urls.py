from django.urls import path
from . import views

urlpatterns = [
    path('tracking/', views.tracking, name='tracking'),
]
