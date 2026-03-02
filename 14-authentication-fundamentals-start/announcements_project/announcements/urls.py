from django.urls import path
from .views import announcement_list, create_announcement

urlpatterns = [
    # we're using this over here.
    path('', announcement_list, name='announcement_list'),
    path('create/', create_announcement, name='create_announcement'),
]
