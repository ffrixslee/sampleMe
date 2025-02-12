from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("logOn.urls")),  # Add your app's URL to connect the app and the project
]
