class Product:
    def __init__(self, name: str, weight: float, category: str):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name of product must be a str', name)
        if isinstance(category, str):
            self.category = category
        else:
            raise ValueError('Name of category must be a str', category)
        if isinstance(weight, (int, float)):
            self.weight = weight
        else:
            raise ValueError('Weight must be an int or float', weight)

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self) -> str:
        get_products = open(self.__file_name).read()
        return get_products

    def add(self, *products: Product) -> None:
        list_products = [*products]
        for i in list_products:
            write_product = open(self.__file_name, 'a')
            if i.name not in self.get_products():
                write_product.write(f'{i.name}, {i.weight}, {i.category} \n')
            else:
                print(f'Продукт {i} уже есть в магазине ')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
