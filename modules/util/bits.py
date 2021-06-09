""" Contains class and functions for Bit Manipulation """


class BitUtils(object):
    """ Contains utility functions for bitwise operations """

    @staticmethod
    def rotate_left(number, rotations=1, field_width=32):
        """
        Performs a specific number of bitwise left rotations on a given number
        :param number: the number/operand
        :param rotations: the number of bitwise left rotations
        :param field_width: the machine field width
        :return:
        """
        efw = 2 ** field_width - 1
        rfw = rotations % field_width
        return ((number << rfw) & efw) | ((number & efw) >> (field_width - rfw))

    @staticmethod
    def rotate_right(number, rotations=1, field_width=32):
        """
        Performs a specific number of bitwise right rotations on a given number
        :param number: the number/operand
        :param rotations: the number of bitwise right rotations
        :param field_width: the machine field width
        :return:
        """
        efw = 2 ** field_width - 1
        rfw = rotations % field_width
        return ((number & efw) >> rfw) | (number << (field_width - rfw) & efw)
