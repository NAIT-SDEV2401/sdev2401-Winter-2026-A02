# we need the settings to configure the urls.
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('core.urls')),  # registration view added!
    path('announcements/', include('announcements.urls')),  # announcements app urls
]

# we need to serve these files as urls
if settings.DEBUG: # our development settings
    urlpatterns += static(
        settings.MEDIA_URL, # the path to serve
        document_root=settings.MEDIA_ROOT
    )