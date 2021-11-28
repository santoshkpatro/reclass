from rest_framework import status
from rest_framework.exceptions import APIException
from reclass.models.subject import Subject


class SubjectEnrolledMixin:
    def get_subject(self):
        subject_id = self.request.query_params['subject_id']
        try:
            subject = Subject.active_objects.get(id=subject_id)
            # Checking for enrollment
            if not subject in Subject.active_objects.filter(
                    enrollments__user=self.request.user):
                raise APIException(
                    detail='Unauthorized access',
                    code=status.HTTP_401_UNAUTHORIZED
                )
            return subject
        except Subject.DoesNotExist:
            raise APIException(
                detail='Subject does not exists',
                code=status.HTTP_404_NOT_FOUND
            )

    def get_subjects(self):
        return Subject.active_objects.filter(
            enrollments__user=self.request.user)
