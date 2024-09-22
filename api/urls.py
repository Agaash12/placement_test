from django.urls import path
from .views import bfhl_api

urlpatterns = [
    path('bfhl/', bfhl_api, name='bfhl_api'),  # Define the route for bfhl API
]
