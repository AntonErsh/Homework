data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(a):
    sum_sum = 0
    if isinstance(a, int):  # Числа
        sum_sum += a
    elif isinstance(a, str):  # Строки
        sum_sum += len(a)
    elif isinstance(a, (list, tuple, set)):  # Список, кортеж, множества
        for i in a:
            sum_sum += calculate_structure_sum(i)
    elif isinstance(a, dict):  # Словарь
        for i in a.keys():  # Ключи
            sum_sum += len(i)
        for i in a.values():  # Значения
            sum_sum += i

    return sum_sum


result = calculate_structure_sum(data_structure)
print(result)
