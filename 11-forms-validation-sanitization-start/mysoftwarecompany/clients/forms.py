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

    # is we're going to perform a little more validation.
    # check to see if the name is greater than 2 characters.
    def clean_name(self):
        # get the cleaned name here (from the cleaned_data dict)
        name = self.cleaned_data.get('name')

        if len(name) < 2:
            # if it's lessa than two we're going to raise a validation error.
            raise forms.ValidationError(
                "name must be greater than 2 characters"
            )
        # otherwise return the name.
        return name