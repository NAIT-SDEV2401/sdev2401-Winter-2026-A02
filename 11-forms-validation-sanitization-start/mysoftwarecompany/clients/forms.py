# let's import forms module from django
from django import forms

# create a contact form.
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(
        widget=forms.Textarea, required=True
    )
