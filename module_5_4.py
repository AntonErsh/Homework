class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return "Неверный ввод!"

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return "Неверный ввод!"

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors <= other
        elif isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return "Неверный ввод!"

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return "Неверный ввод!"

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other
        elif isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return "Неверный ввод!"

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other
        elif isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return "Неверный ввод!"

    def __add__(self, other):
        if isinstance(other, int) and other > 0:
            self.number_of_floors += other
            return self
        elif isinstance(other, House):
            self.number_of_floors += other.number_of_floors
            return self
        else:
            return "Неверный ввод!"

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует ')
        else:
            i = 1
            while i <= new_floor:
                print(i)
                i += 1

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


house_1 = House('ЖК Янино-1', 10)
print(House.houses_history)
house_2 = House('Меркурий-Сити', 75)
print(House.houses_history)
house_3 = House('Шалаш', 1)
print(House.houses_history)
# print(1, house_1)
# print(2, house_2)
# print(3, house_1 == house_2)  # __eq__
# house_1 = house_1 + 10  # __add__
# print(4, house_1)
# house_1 += 55  # __iadd__
# print(5, house_1)
# print(12, house_1 == house_2)
# house_2 = 10 + house_2  # __radd__
# print(6, house_2)
# print(7, house_1 > house_2)  # __gt__
# print(8, house_1 >= 10)  # __ge__
# print(9, house_1 < house_2)  # __lt__
# print(10, house_1 <= house_2)  # __le__
# print(11, house_1 != house_2)  # __ne__
del house_2
del house_1
print(House.houses_history)
