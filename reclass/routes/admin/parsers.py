from rest_framework.parsers import BaseParser


class FileParser(BaseParser):
    media_type = '*/*'
