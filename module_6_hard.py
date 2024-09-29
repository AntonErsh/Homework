import math
from typing import List


class Figure:
    sides_count = 0

    def __init__(self, sides: list[float], color: list[int], filled: bool = True):
        self.__sides = sides
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            raise ValueError('Числа цветов должны быть в диапазоне от 1 до 255 ', color)
        if filled == bool:
            self.filled = filled

    def get_color(self) -> list[int]:
        return self.__color

    @staticmethod
    def __is_valid_color(r: int, g: int, b: int) -> tuple[int, int, int]:
        if 0 < (r or g or b) <= 255:
            return r, g, b

    def set_color(self, r: int, g: int, b: int) -> None:
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self) -> bool:
        if len(self.__sides) <= self.sides_count:
            side = 0
            while side <= len(self.__sides) + 1:
                if side == len(self.__sides):
                    return True
                if self.__sides[side] > 0:
                    side += 1
            return False

    def get_sides(self) -> list[float]:
        return self.__sides

    def __len__(self) -> int:
        return sum(self.__sides)

    def set_sides(self, *new_sides: int) -> None:
        new_sides = [*new_sides]
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, sides: list[float], color: list[int], filled: bool = True):
        if len(sides) == self.sides_count:
            self.__sides = sides
            self.__radius = sum(sides) / 2
        else:
            self.__sides = [1]
            self.__radius = 0.5
        super().__init__(sides, color, filled)

    def get_square(self) -> float:
        return round(3.1415 * (self.__radius**2), 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides: list[float], color: list[int], filled: bool = True):
        if len(sides) == self.sides_count:
            if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
                self.__sides = sides
            else:
                raise ValueError('Ошибка, сумма длин каждых двух сторон должна быть больше длины третьей стороны')
        else:
            self.__sides = [1] * self.sides_count
        super().__init__(sides, color, filled)

    def get_square(self) -> float:
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]
        p = sum(self.__sides) / 2
        for_sqrt = p * (p - a) * (p - b) * (p - c)
        square_of_triangle = round(math.sqrt(for_sqrt), 2)
        return square_of_triangle


class Cube(Figure):
    sides_count = 1

    def __init__(self, sides: list[float], color: list[int], filled: bool = True):
        if len(sides) == self.sides_count:
            self.__sides = sides * 12
            self.side = sum(sides)
        else:
            self.__sides = [1] * 12
        super().__init__(sides, color, filled)

    def get_volume(self) -> float:
        return self.side**3


circle1 = Circle([10], [200, 200, 100])
circle2 = Circle([10.2, 2], [200, 200, 100])
cube1 = Cube([2], [200, 200, 200], True)
triangle1 = Triangle([10, 5, 6], [150, 100, 150], False)
print(circle1.get_square())
print(circle2.get_square())
print(triangle1.get_square())
print(cube1.get_volume())
print(triangle1.get_color())
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
print(len(circle1))
