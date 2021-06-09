"""
Contains validators for common string formats
"""
from os import path
from urllib.parse import urlparse


class Validators(object):
    @staticmethod
    def is_valid_file(file_path=None):
        if not file_path or not path.exists(file_path) or not path.isfile(file_path):
            return False
        else:
            return True

    @staticmethod
    def is_url(url=''):
        try:
            result = urlparse(url)
            return True if [result.scheme, result.netloc, result.path] else False
        except Exception:
            return False

    @staticmethod
    def is_http_method(method=''):
        return method in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'TRACE', 'OPTIONS']
