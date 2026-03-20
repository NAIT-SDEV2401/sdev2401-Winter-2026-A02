from django.urls import path

from .views import (
    bulk_assignment_upload,
    assignment_list,
    assignment_submission,
    AssignmentListView,
    AssignmentSubmissionView,
    BulkAssignmentUploadView,
)

urlpatterns = [
    path(
        "bulk-assignment-upload/",
        BulkAssignmentUploadView.as_view(),
        name="bulk_assignment_upload",
    ),
    # path(
    #     "bulk-assignment-upload/", bulk_assignment_upload, name="bulk_assignment_upload"
    # ),
    path(
        "assignments/",
        AssignmentListView.as_view(),
        name="assignment_list",
    ),
    # path("assignments/", assignment_list, name="assignment_list"),
    path(
        "assignments/<int:assignment_id>/submit/",
        AssignmentSubmissionView.as_view(),
        name="assignment_submission",
    ),
    # path(
    #     "assignments/<int:assignment_id>/submit/",
    #     assignment_submission,
    #     name="assignment_submission",
    # ),
]
