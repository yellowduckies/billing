from rest_framework import permissions


class IsEmployeeOrCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.myuser.user_role == 'emp'

class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

class IsAllowedToViewOnlyToOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.myuser.user_role == 'emp'

    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return True
        return False