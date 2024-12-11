import unittest
from rectangle import area, perimeter
from unittest.mock import patch

class RectangleTestCase(unittest.TestCase):
    '''area'''
    @patch("builtins.print")
    def test_area_zero_side(self, mock_print):
        res = area(0, 10)
        mock_print.assert_called_once_with("Ошибка: обе стороны должны быть положительны")
        self.assertIsNone(res)

    def test_area_positive_side(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    @patch("builtins.print")
    def test_area_negative_side(self, mock_print):
        res = area(-10, 5)
        mock_print.assert_called_once_with("Ошибка: обе стороны должны быть положительны")
        self.assertIsNone(res)

    def test_area_float_side(self):
        res = area(1.5, 2.5)
        self.assertEqual(res, 3.75)

    '''perimeter'''
    @patch("builtins.print")
    def test_perimeter_zero_side(self, mock_print):
        res = perimeter(10, 0)
        mock_print.assert_called_once_with("Ошибка: обе стороны должны быть положительны")
        self.assertIsNone(res)

    def test_perimeter_positive_side(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)

    @patch("builtins.print")
    def test_perimeter_negative_side(self, mock_print):
        res = perimeter(10, -10)
        mock_print.assert_called_once_with("Ошибка: обе стороны должны быть положительны")
        self.assertIsNone(res)

    def test_perimeter_float_side(self):
        res = perimeter(1.5, 2.5)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()