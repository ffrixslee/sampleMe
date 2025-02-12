from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),  # Django auth URLs for login/logout
    path("", include("logOn.urls")),  # Add your app's URL
]
