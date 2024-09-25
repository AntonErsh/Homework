class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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
house_1.go_to(8)
house_2.go_to(64)
house_3.go_to(3)
