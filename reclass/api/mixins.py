from reclass.api.exceptions import GroupNotFoundException, AuthorizationException
from reclass.models import Group


class GroupEnrolledMixin:
    def get_group(self):
        group_id = self.request.query_params.get('group_id', None)
        if group_id is None:
            raise GroupNotFoundException
        try:
            group = Group.active_objects.get(pk=group_id)
            enrolled_groups = Group.active_objects.filter(
                group_enrollments__user=self.request.user, 
                group_enrollments__is_active=True
            )
            if not group in enrolled_groups:
                raise AuthorizationException
            return group
        except Group.DoesNotExist:
            raise GroupNotFoundException


class GroupMixin:
    def get_group(self):
        group_id = self.request.query_params.get('group_id', None)
        if group_id is None:
            raise GroupNotFoundException
        try:
            group = Group.active_objects.get(pk=group_id)
            return group
        except Group.DoesNotExist:
            raise GroupNotFoundException