def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_ = []
        matrix.append(list_)
        for j in range(m):
            list_.append(value)
    return matrix


result1 = get_matrix(2, 2, 25)
result2 = get_matrix(3, 4, 70)
result3 = get_matrix(5, 5, 49)
result4 = get_matrix(0, 5, 10)
print(result1)
print(result2)
print(result3)
print(result4)
