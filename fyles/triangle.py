def area(a, h):
    '''принимает числа a (основание треугольника) и h (высота треугольника) и возвращает его площадь '''
    if a < 0 or h < 0:
        raise ValueError("основание и высота не могут быть отрицательными")
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("основание и высота должны быть числами")
    return 0.5 * a * h


def perimeter(a):
    '''принимает числа a (сторону треугольника) и возвращает его периметр'''
    if a < 0 :
        raise ValueError("сторона треугольника не могут быть отрицательными")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("сторона треугольника должны быть числами")
    return a + b + c