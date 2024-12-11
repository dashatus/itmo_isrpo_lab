import unittest
from circle import area, perimeter
from unittest.mock import patch

class CircleTestCase(unittest.TestCase):
    '''area'''
    @patch("builtins.print")
    def test_area_zero_radius(self, mock_print):
        res = area(0)
        mock_print.assert_called_once_with("Ошибка: радиус должен быть положительным")
        self.assertIsNone(res)

    def test_area_positive_radius(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.1592653589793)

    @patch("builtins.print")
    def test_area_negative_radius(self, mock_print):
        res = area(-10)
        mock_print.assert_called_once_with("Ошибка: радиус должен быть положительным")
        self.assertIsNone(res)

    def test_area_float_radius(self):
        res = area(1.5)
        self.assertAlmostEqual(res, 7.068583470577034)

    '''perimeter'''
    @patch("builtins.print")
    def test_perimeter_zero_radius(self, mock_print):
        res = perimeter(0)
        mock_print.assert_called_once_with("Ошибка: радиус должен быть положительным")
        self.assertIsNone(res)

    def test_perimeter_positive_radius(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.83185307179586)

    @patch("builtins.print")
    def test_perimeter_negative_radius(self, mock_print):
        res = perimeter(-10)
        mock_print.assert_called_once_with("Ошибка: радиус должен быть положительным")
        self.assertIsNone(res)

    def test_perimeter_float_radius(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, 9.424777960769379)

if __name__ == '__main__':
    unittest.main()