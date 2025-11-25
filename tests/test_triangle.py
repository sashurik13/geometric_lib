
import unittest
import math

from fyles.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    #площадь
    def test_area_positive_int(self): # стандартные типы int
        self.assertEqual(area(5, 3), 15)
        self.assertEqual(area(120, 10), 1200)

    def test_area_positive_float(self): # для float данных
        self.assertAlmostEqual(area(5.7, 3.3), 18.81, places=7)
        self.assertAlmostEqual(area(3.125, 4.183), 13.071875, places=7)

    def test_area_zero(self): #проверка на 0
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 6789), 0)

    def test_area_negative_radius(self): #проверка на отрицательные числа
        with self.assertRaises(ValueError):
            area(-10, -190)
        with self.assertRaises(ValueError):
            area(-3.4039, -783)
        with self.assertRaises(ValueError):
            area(3.4039, -783)  

    def test_area_big_numbers(self): # проверка на очень большие числа
        self.assertAlmostEqual(area(18000000, 90000), 1620000000000, places=0)
        self.assertAlmostEqual(area(2500, 2500000), 62500000000, places=0)
    

    #периметр
    #далее функции анаогичные, только для периметра
    def test_perimeter_positive_integer(self):
        self.assertEqual(perimetr(4), 12)
        self.assertEqual(perimetr(9), 27)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(perimetr(3.5), 10.5, places=7)
        self.assertAlmostEqual(perimetr(2.8), 8.4, places=7)

    def test_perimeter_zero(self):
        self.assertEqual(perimetr(0), 0)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimetr(-6)
        with self.assertRaises(ValueError):
            perimetr(-2.5)

    def test_perimeter_large_numbers(self):
        self.assertEqual(perimetr(10000000000), 30000000000)

if __name__ == '__main__':
    unittest.main()
