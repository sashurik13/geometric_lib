def area(a):
    '''принимает число а (длина стороны квадрата) и возвращает его площадь '''
    if a < 0:
        raise ValueError("сторона квадрата не может быть отрицательной")
    if not isinstance(a, (int, float)):
        raise TypeError("сторона квадрата должна быть числом")
    return a * a


def perimeter(a):
    '''принимает число а (длина стороны квадрата) и возвращает его периметр'''
    if a < 0:
        raise ValueError("сторона квадрата не может быть отрицательной")
    if not isinstance(a, (int, float)):
        raise TypeError("сторона квадрата должна быть числом")
    return 4 * a