# we're going to create a permission
# that users can read the data but not change the data if it's not theirs.

# we're going to need to import from BasePermission from rest framework.
from rest_framework.permissions import BasePermission


class IsOwnerOfResourceOrReadOnly(BasePermission):
    """
    Custom permission that allows only the owners of the model instance
    to update that item.
    """

    # has object permission is the permission on a specific object.
    # returns true or false, true if they have permission, false if they don't.
    def has_object_permission(self, request, view, obj):
        # we're going to check if the request.method is going to be a "safe method"
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        # if hits this point it'll be "PUT"/"POST"/"PATCH" request
        # note 1: the model needs a user field
        # note 2: we will compare that user to the request.user field
        # this is taken from the token provided.
        return obj.user == request.user
