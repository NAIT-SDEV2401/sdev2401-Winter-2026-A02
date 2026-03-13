from django import forms


# this is going to take a file that's a csv
# ensure that it's a csv in our validation
# in our model we're going to import all of the items.
class BulkAssignmentUploadForm(forms.Form):
    csv_file = forms.FileField(
        label="Select a CSV",
    )

    # Let's add some validation on this file.
    def clean_csv_file(self):
        breakpoint()
        file = self.cleaned_data.get("csv_file")
        # check a few properties of the file.
        # like the file type extension.
        if not file.name.endswith(".csv"):
            raise forms.ValidationError(
                "Please upload a CSV file",
            )

        # check the content type of the file.
        if file.content_type != "text/csv":
            raise forms.ValidationError("File type is not CSV.")

        return file
