from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class IsOwnerOrAdmin(permissions.BasePermission):
    message = 'You do not have permission to perform this action.'
    def has_permission(self, request, view):
        return view.action != "list" or request.user.is_superuser
    def has_object_permission(self, request, view, obj):
        return (request.user.user_card == obj) or request.user.is_superuser
