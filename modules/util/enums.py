"""
Contains enumeration utility functions
"""


class EnumUtils(object):
    @staticmethod
    def for_name(name='', enum_type=None, enum_description=''):
        """
        Returns the enum constant with the specified name
        :param name: the name of the enum constant
        :param enum_type: the type of the enum constant
        :param enum_description: description of the enum
        :return: matching enum constant
        """
        found = None
        _name = name.upper()

        try:
            found = enum_type[_name]
        except Exception:
            raise ValueError("Unsupported {0} {1}".format(enum_description, name))

        return found
