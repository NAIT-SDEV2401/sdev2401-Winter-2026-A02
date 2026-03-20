from django.urls import path
from .views import (
    announcement_list,
    create_announcement,
    AnnouncementListView,
    CreateAnnouncementView,
)

urlpatterns = [
    # the cbv way for urls
    path(
        "",
        AnnouncementListView.as_view(),
        name="announcement_list",
    ),
    # the function based way below
    # path('', announcement_list, name='announcement_list'),
    path(
        "create/",
        CreateAnnouncementView.as_view(),
        name="create_announcement",
    ),
    # the FBV
    # path("create/", create_announcement, name="create_announcement"),
]
