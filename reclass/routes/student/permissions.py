from rest_framework import permissions
from reclass.models import Subject


class IsEnrolled(permissions.BasePermission):
    # message = 'Unauthorized access'

    def has_object_permission(self, request, view, obj):
        if not obj.subject in Subject.active_objects.filter(enrollments__user=request.user):
            return False
        return True


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
