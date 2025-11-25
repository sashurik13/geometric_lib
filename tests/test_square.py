import unittest
import math

from fyles.square import area, perimeter

class SquareTestCase(unittest.TestCase):
    #площадь
    def test_area_positive_int(self): # стандартные типы int
        self.assertEqual(area(5), math.pi * 25)
        self.assertEqual(area(120), math.pi * 14400)

    def test_area_positive_float(self): # для float данных
        self.assertAlmostEqual(area(5.7), math.pi * 32.49, places=7)
        self.assertAlmostEqual(area(3.125), math.pi * 9.765625, places=7)

    def test_area_zero(self): #проверка на 0
        self.assertEqual(area(0), 0)

    def test_area_negative_radius(self): #проверка на отрицательные числа
        with self.assertRaises(ValueError):
            area(-10)
        with self.assertRaises(ValueError):
            area(-3.4039)
            
    def test_area_big_numbers(self): # проверка на очень большие числа
        self.assertAlmostEqual(area(18000000), math.pi * 18000000 ** 2, places=0)
        self.assertAlmostEqual(area(2500000000), math.pi * 2500000000 ** 2, places=0)

    def test_area_small_numbers(self):# проверка на очень маленькие числа
        self.assertAlmostEqual(area(2e-6), math.pi * 2e-6 * 2e-6, places=15)
        self.assertAlmostEqual(area(5e-9), math.pi * 5e-9 * 5e-9, places=15)
    

    #периметр
    #далее функции анаогичные, только для периметра
    def test_perimeter_positive_integer(self):
        self.assertEqual(perimetr(4), 2 * math.pi * 4)
        self.assertEqual(perimetr(9), 2 * math.pi * 9)
        self.assertEqual(perimetr(15), 2 * math.pi * 15)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(perimetr(3.5), 2 * math.pi * 3.5, places=7)
        self.assertAlmostEqual(perimetr(2.8), 2 * math.pi * 2.8, places=7)
        self.assertAlmostEqual(perimetr(6.75), 2 * math.pi * 6.75, places=7)

    def test_perimeter_zero(self):
        self.assertEqual(perimetr(0), 0)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimetr(-6)
        with self.assertRaises(ValueError):
            perimetr(-12)
        with self.assertRaises(ValueError):
            perimetr(-2.5)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            perimetr("diameter")
        with self.assertRaises(TypeError):
            perimetr({"r": 5})

    def test_perimeter_large_numbers(self):
        self.assertEqual(perimetr(10000000000), 2 * math.pi * 10000000000)
        self.assertEqual(perimetr(98789676), 2 * math.pi * 98789676)

if __name__ == '__main__':
    unittest.main()
