class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

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


house_1 = House('ЖК Янино-1', 10)
house_2 = House('Меркурий-Сити', 75)
house_3 = House('Шалаш', 1)
print(house_1)
print(house_2)
print(house_3)
print(len(house_1))
print(len(house_2))
print(len(house_3))
