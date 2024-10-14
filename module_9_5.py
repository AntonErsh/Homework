class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start: int, stop: int, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0', step)
        else:
            self.step = step
        self.start = start - step
        self.stop = stop + step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0 and (self.pointer > self.stop or (self.pointer + self.step) > self.stop):
            raise StopIteration()
        if self.step < 0 and (self.pointer < self.stop or (self.pointer + self.step) < self.stop):
            raise StopIteration()
        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
result = []
for i in iter2:
    result.append(i)
print(result)
result.clear()
for i in iter3:
    result.append(i)
print(result)
result.clear()
for i in iter4:
    result.append(i)
print(result)
result.clear()
for i in iter5:
    result.append(i)
print(result)
