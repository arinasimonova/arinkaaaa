Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Shape:
...     def area(self):
...         return 0
... 
... class Rectangle(Shape):
...     def __init__(self, width, height):
...         self.width = width
...         self.height = height
... 
...     def area(self):
...         return self.width * self.height
... 
... class Rhombus(Shape):
...     def __init__(self, diagonal1, diagonal2):
...         self.diagonal1 = diagonal1
...         self.diagonal2 = diagonal2
... 
...     def area(self):
...         return 0.5 * self.diagonal1 * self.diagonal2
... 
... class Circle(Shape):
...     def __init__(self, radius):
...         self.radius = radius
... 
...     def area(self):
...         return 3.14 * (self.radius ** 2)
... 
... # Создание объектов с новыми данными
... rectangle = Rectangle(8, 10)
... rhombus = Rhombus(6, 4)
... circle = Circle(7)
... 
... # Вывод результатов
... print("Площадь прямоугольника:", rectangle.area())
... print("Площадь ромба:", rhombus.area())
... print("Площадь круга:", circle.area())
