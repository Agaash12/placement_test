from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface route
    path('api/', include('api.urls')),  # Include the API routes defined in the app's urls.py
]
