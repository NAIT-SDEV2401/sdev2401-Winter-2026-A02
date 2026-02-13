# let's import forms module from django
from django import forms

# create a contact form.
class ContactForm(forms.Form):
    name =