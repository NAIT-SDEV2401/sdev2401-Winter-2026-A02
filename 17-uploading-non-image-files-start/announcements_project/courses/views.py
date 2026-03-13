from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import BulkAssignmentUploadForm
from .models import Assignment

# create our bulk assingment upload view


# create the view
# that uses the form that we just created
# the get file from the cleaned data
@login_required
def bulk_assignment_upload(request):
    success = False
    if request.method == "POST":
        form = BulkAssignmentUploadForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid():
            csv_file = form.cleaned_data.get("csv_file")
            # let's call our class method
            assignments = Assignment.create_assignments_from_csv(
                csv_file=csv_file,
                owner=request.user,
            )
            success = True
            # next class we're going to build the parser
            # that's going to create a whole bunch of assignments
            # render that in the template.

    else:
        form = BulkAssignmentUploadForm()

    return render(
        request,
        "courses/bulk_assignment_upload.html",
        {
            "form": form,
            "assignments": assignments,
            "success": success,
        },
    )
