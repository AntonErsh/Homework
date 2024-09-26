class Vehicle:
    __COLOR_VARIANTS = ['White', 'Black', 'Blue', 'Turquoise', 'Red']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.capitalize() not in self.__COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на {new_color.capitalize()}')
            return
        for i in self.__COLOR_VARIANTS:
            if new_color.lower() == i.lower():
                self.__color = new_color
                return


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'Blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
