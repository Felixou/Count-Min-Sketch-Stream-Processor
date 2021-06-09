from unittest import TestCase, main

from modules.util.bits import *


class TestBitUtils(TestCase):
    def test_rotate_left(self):
        """Test bit_rotate_left"""
        expected = [32, 512, 8192, 131072]
        actual = []

        n = 2
        for i in range(0, 4):
            n = BitUtils.rotate_left(n, 4)
            actual.append(n)

        self.assertTrue(actual)
        self.assertEqual(len(actual), len(expected))
        self.assertEqual(actual, expected)

    def test_rotate_right(self):
        """Test bit_rotate_right"""
        expected = [131072, 8192, 512, 32]
        actual = []

        n = 2097152
        for i in range(0, 4):
            n = BitUtils.rotate_right(n, 4)
            actual.append(n)

        self.assertTrue(actual)
        self.assertEqual(len(actual), len(expected))
        self.assertEqual(actual, expected)


# run the tests suite
if __name__ == "__main__":
    main()
