from django.urls import path
from .views import login, logout_view  # Import the correct view

urlpatterns = [
    path('', login, name='login'),  # Login page URL
    path('logout/', logout_view, name='logout'),  # Logout URL
]
