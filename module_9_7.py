def is_prime(func):
    def wrapper(a, b, c):
        result1 = func(a, b, c)
        flag = True
        for i in range(2, (result1 // 2) + 1):
            if result1 == (1 or 2 or 3):
                break
            elif result1 % i == 0:
                flag = False
                break
        if flag is False:
            print('Составное')
        else:
            print("Простое")
        return result1
    return wrapper


@ is_prime
def sum_three(a: int, b: int, c: int):
    sum_abc = a + b + c
    return sum_abc


result = sum_three(3, 12, 52)
print(result)
