from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/professionals", include("professionals.urls")),
    path("api/appointments", include("appointments.urls")),
]
