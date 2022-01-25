from email.policy import default
from rest_framework.exceptions import APIException


class UserNotFoundException(APIException):
    status_code = 404
    default_detail = 'User not found.'
    default_code = 'not found'


class GroupNotFoundException(APIException):
    status_code = 404
    default_detail = 'Group not found.'
    default_code = 'not found'


class AuthorizationException(APIException):
    status_code = 401
    default_detail = 'You are not authorized to perform this action'
    default_code = 'not authrized.'