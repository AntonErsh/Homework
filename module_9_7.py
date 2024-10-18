def is_prime(func):
    def wrapper(a, b, c):
        result1 = func(a, b, c)
        for i in range(2, (result1 // 2) + 1):
            if result1 % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return result1
    return wrapper


@ is_prime
def sum_three(a: int, b: int, c: int):
    sum_abc = a + b + c
    return sum_abc


result = sum_three(1, 5, 11)
print(result)
