insert_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = ''
zero = 0
n = int(input('Введите целое число от 3 до 20 '))
if n in insert_1:
    for j in range(1, n):
        for k in range(j+1, n):
            if n % (j + k) == 0:
                result = result + str(j) + str(k)
    print('Код: ', result)
else:
    print('Необходимо ввести целое число в диапазоне от 3 до 20')
