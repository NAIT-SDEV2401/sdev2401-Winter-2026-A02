from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import BulkAssignmentUploadForm, SubmissionForm
from .models import Assignment


@login_required
def assignment_list(request):
    assignments = Assignment.objects.all().order_by("-created_at")
    return render(
        request,
        "courses/assignment_list.html",
        {
            "assignments": assignments,
        },
    )


@login_required
def assignment_submission(request, assignment_id):
    # fix this view.
    # get the assignment first
    assignment = get_object_or_404(
        Assignment,
        id=assignment_id,
    )
    if request.method == "POST":
        # create a form with the right fields
        form = SubmissionForm(request.POST, request.FILES)
        # handle the form and it's files
        if form.is_valid():
            instance = form.submit(commit=False)
            # we need to add the assignment
            instance.assignment = assignment
            # save the data
            instance.save()
        # give link to the submission on success and a short message.
    else:
        form = SubmissionForm()
    # render that form in a template (look at bulk_assignment_upload.html for help)
    return render(
        request,
        "courses/assignment_submission.html",
        {
            "assignment_id": assignment_id,
            "form": form,
        },
    )


# Create your views here.
@login_required
def bulk_assignment_upload(request):
    success = False
    assignments = []
    if request.method == "POST":
        form = BulkAssignmentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded CSV file
            csv_file = form.cleaned_data["csv_file"]
            # Create assignments from the CSV file
            assignments = Assignment.create_assignments_from_csv(
                csv_file, owner=request.user
            )
            # Note
            success = True
    else:
        form = BulkAssignmentUploadForm()

    return render(
        request,
        "courses/bulk_assignment_upload.html",
        {
            "form": form,
            "success": success,
            "assignments": assignments,
        },
    )
