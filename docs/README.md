# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Общее описание решения
Были реализованы функции для определения:
- периметра
- площади 

Для четырех геометрических фигур, таких как:
- круг
- квадрат
- треугольник
- прямоугольник

# Описание функций
## rectangle.py
`area(a, b)`
- Получает на вход длины двух сторон прямоугольника
- Возвращает площадь прямоугольника `return a * b`
- Пример вызова функции: `s = area(3, 5)`

`perimeter(a, b)`
- Получает на вход длины двух сторон прямоугольника
- Возвращает периметр прямоуголька `return (a + b)*2`
- Пример вызова функции: `p = perimetr(3, 5)`
## triangle.py
`area(a, h)`
- Получает на вход длины основания и высоты треугольника
- Возвращает площадь треугольника `return a * h / 2 `
- Пример вызова функции: `s = area(3, 5)`

`perimeter(a, b, c)`
- Получает на вход длины всех сторон треугольника
- Возвращает периметр треугольника `return a + b + c`
- Пример вызова функции: `p = perimetr(3, 4, 5)`
## circle.py
`import math` - включение библиотеки для использования константы пи

`area(r)`
- Получает на вход длину радиуса окружности
- Возращает площадь круга `return math.pi * r * r`
- Пример вызова функции: `s = area(5)`

`perimeter(r)`
- Получает на вход длину радиуса окружности
- Возвращает длину окружности `return 2 * math.pi * r`
- Пример вызова функции: `p = perimetr(5)`
## square.py
`area(a)`
- Получает на вход длину стороны квадрата
- Возвращает площадь квадрата `return a * a`
- Пример вызова функции: `s = area(5)`

`perimeter(a)`
- Получает на вход длину стороны квадрата
- Возвращает периметр квадрата `return 4 * a`
- Пример вызова функции: `p = perimetr(5)`

# История изменения проекта
- **f9d967d (HEAD -> new_features_407638, origin/new_features_407638, origin/HEAD) Add workflow for testing**
коммит о добавлении workflow
- **51a2aa4 added tests**
коммит о добавлении модульных тестов
- **41b5940 added checking for correct args**
коммит о добавлении проверки корректности параметров в функциях нахождения площадей и периметров
- **7444cdd comments've been added to the files rectangle.py, triangle.py, circle.py, square.py**
коммит о добавлениях блока комментариев в файлы rectangle.py, triangle.py, circle.py, square.py
- **071027e rectangle.py fixed**
коммит об исправлении ошибки вычисления периметра прямоугольника (+ добавление нового файла triangle.py)
- **3bc97d0 file rectangle.py has been added**
коммит о добавлениии нового файла rectangle.py
- **d078c8d (origin/main, origin/HEAD, main) L-03: Docs added**
- **8ba9aeb L-03: Circle and square added**