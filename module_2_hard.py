insert_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
insert_2 = []
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
number = insert_1[0]
zero = 0

while zero < len(insert_1):
    for i in insert_1:
        for j in list_:
            for k in list_:
                if i % j + k == 0:
                    print(f'{j} + {k}')
                    continue
                else:
                    print('not')
        zero += 1
