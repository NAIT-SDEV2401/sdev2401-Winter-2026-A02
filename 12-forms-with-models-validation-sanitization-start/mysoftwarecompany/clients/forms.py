from django import forms

# create a model form based on the Company model.
from .models import Company

class CompanyForm(forms.ModelForm):
    # meta class tells django what model and fields to use.
    class Meta:
        model = Company
        fields = ['name', 'email', 'description']
        # we don't add created_at and updated_at because these get updated
        # on their own.

    # let's add some cross field validation
    # validation on multiple fields here.
    def clean(self):
        # list of banned wordss
        forbidden_words = ["scam", "fake", "ponzi"]
        # get the cleaned data from the super class which
        # is the forms.Modelform
        cleaned_data = super().clean() # a dictionary
        # name and description
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')


        for word in forbidden_words:
            if (word in description.lower() or
                word in name.lower()):
                raise forms.ValidationError(
                    F"word '{word}' is forbidden please change"
                )

        return cleaned_data



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # Custom validation for the name field
    # the <fieldname> method is used to add custom validation to a field.
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            # this will raise an validation error if the name is less than 2 characters long.
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name

    # Custom validation for the message field
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message