from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("core.urls")),  # registration view added!
    path("announcements/", include("announcements.urls")),  # announcements app urls
    path("profiles/", include("profiles.urls")),  # profiles app urls
    path("courses/", include("courses.urls")),  # courses app urls
    # let's add this path
    path("", include("web.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
