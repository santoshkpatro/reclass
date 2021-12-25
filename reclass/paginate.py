from rest_framework.pagination import LimitOffsetPagination


class Pagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 200
