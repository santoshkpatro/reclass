
import os
import mimetypes
from django.conf import settings


def file_extension(file):
    return mimetypes.guess_extension(mimetypes.guess_type(file)[0])


def handle_file_upload(file_obj, file_name):
    file_url = f'{settings.MEDIA_URL}{file_name}'
    file_path = f'{settings.MEDIA_ROOT}/{file_name}'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        fout = open(file_path, 'wb+')
        for chunk in file_obj:
            fout.write(chunk)
    finally:
        fout.close()

    return 'http://127.0.0.1:8000' + file_url
