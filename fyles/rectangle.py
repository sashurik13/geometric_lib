def area(a, b):
    '''принимает числа а и b (длина и ширина прямоугольника) и возвращает его площадь '''
    if a < 0 or b < 0:
        raise ValueError("cтороны не могут быть отрицательными")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("cтороны должны быть числами")
    return a * b

def perimeter(a, b):
    '''принимает числа а и b (длина и ширина прямоугольника) и возвращает его периметр'''
    if a < 0 or b < 0:
        raise ValueError("cтороны не могут быть отрицательными")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("cтороны должны быть числами")
    return 2 * (a + b)