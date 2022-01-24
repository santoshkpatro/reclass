from rest_framework import permissions
from reclass.models.group import Group


class IsEnrolledOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        enrolled_groups = Group.active_objects.filter(
            group_enrollments__user=request.user, 
            group_enrollments__is_active=True
        )
        
        if obj not in enrolled_groups and obj.owner != request.user:
            return False

        return True


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner != request.user:
            return False
        return True