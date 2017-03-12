from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif view.action == "list":
            return False
        return True

    def has_object_permission(self, request, view, obj):
        return (request.user.user_card == obj) or request.user.is_superuser
