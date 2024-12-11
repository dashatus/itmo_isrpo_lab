import math


def area(r):
    '''Принимает длину радиуса, возращает площадь круга.'''
    if r <= 0:
        print("Ошибка: радиус должен быть положительным")
        return None
    return math.pi * r * r


def perimeter(r):
    '''Принимает длину радиуса, возвращает длину окружности.'''
    if r <= 0:
        print("Ошибка: радиус должен быть положительным")
        return None
    return 2 * math.pi * r

