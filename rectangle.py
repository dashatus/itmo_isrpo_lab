def area(a, b):
    '''Принимает на вход длины двух сторон прямоугольника, возвращает его площадь.'''
    if (a <= 0) or (b <= 0):
        print("Ошибка: обе стороны должны быть положительны")
        return None
    return a * b 

def perimeter(a, b):
    '''Принимает на вход длины двух сторон прямоугольника, возвращает его периметр.'''
    if (a <= 0) or (b <= 0):
        print("Ошибка: обе стороны должны быть положительны")
        return None
    return (a + b)*2 
