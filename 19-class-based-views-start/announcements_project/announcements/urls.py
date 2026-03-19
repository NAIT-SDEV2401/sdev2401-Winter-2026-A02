from django.urls import path
from .views import announcement_list, create_announcement, AnnouncementListView

urlpatterns = [
    # the cbv way for urls
    path(
        "",
        AnnouncementListView.as_view(),
        name="announcement_list",
    ),
    # the function based way below
    # path('', announcement_list, name='announcement_list'),
    path("create/", create_announcement, name="create_announcement"),
]
