from rest_framework import permissions


class IsEmployeeOrCustomer(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return request.user.myuser.user_role == 'emp'

class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

class IsAllowedToViewOnlyToOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.myuser.user_role == 'emp'
    