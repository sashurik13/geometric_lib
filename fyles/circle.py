import math

def area(r):
    '''принимает число r (радиус окружности) и возвращает ее площадь '''
    if r < 0:
        raise ValueError("радиус не может быть отрицательным")
    if not isinstance(r, (int, float)):
        raise TypeError("радиус должен быть числом")
    return math.pi * r * r

def perimeter(r):
    '''принимает число r (радиус окружности) и возвращает ее периметр '''
    if r < 0:
        raise ValueError("радиус не может быть отрицательным")
    if not isinstance(r, (int, float)):
        raise TypeError("радиус должен быть числом")
    return 2 * math.pi * r