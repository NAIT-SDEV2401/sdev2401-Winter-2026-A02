from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('announcements/', include('announcements.urls')),  # announcements app urls
    path('accounts/', include('core.urls')), # login/register endpoints.
]
