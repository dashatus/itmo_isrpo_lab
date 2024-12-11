import unittest
from square import area, perimeter
from unittest.mock import patch

class SquareTestCase(unittest.TestCase):
    '''area'''
    @patch("builtins.print")
    def test_area_zero_side(self, mock_print):
        res = area(0)
        mock_print.assert_called_once_with("Ошибка: стороны должны быть положительны")
        self.assertIsNone(res)

    def test_area_positive_side(self):
        res = area(10)
        self.assertEqual(res, 100)

    @patch("builtins.print")
    def test_area_negative_side(self, mock_print):
        res = area(-10)
        mock_print.assert_called_once_with("Ошибка: стороны должны быть положительны")
        self.assertIsNone(res)

    def test_area_float_side(self):
        res = area(1.5)
        self.assertEqual(res, 2.25)

    '''perimeter'''
    @patch("builtins.print")
    def test_perimeter_zero_side(self, mock_print):
        res = perimeter(0)
        mock_print.assert_called_once_with("Ошибка: стороны должны быть положительны")
        self.assertIsNone(res)

    def test_perimeter_positive_side(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    @patch("builtins.print")
    def test_perimeter_negative_side(self, mock_print):
        res = perimeter(-10)
        mock_print.assert_called_once_with("Ошибка: стороны должны быть положительны")
        self.assertIsNone(res)

    def test_perimeter_float_side(self):
        res = perimeter(1.5)
        self.assertEqual(res, 6)

if __name__ == '__main__':
    unittest.main()