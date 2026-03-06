from django import forms

from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = [ 'title', 'message' ]

        # we're going to use the title and message
        # we're going to add the created_by later on.