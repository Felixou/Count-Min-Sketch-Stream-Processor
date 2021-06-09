from os import path

from pathlib import Path


class FileUtils:
    application_directory = Path().resolve()

    @staticmethod
    def get_absolute_path(file_path=''):
        """
        Returns the absolute file path for a specified file path
        :param file_path: the file path
        :return: the absolute file path
        """
        file_path = file_path.strip()
        if not path.isabs(file_path):
            return "{0}/{1}".format(FileUtils.application_directory, file_path)
        else:
            return file_path
