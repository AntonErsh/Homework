from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count: int, file_name: str) -> None:
    with open(f'{file_name}', 'w', encoding='utf-8') as file:
        i = 0
        while i < word_count:
            file.write(f'Какое-то слово №{i + 1} \n')
            i += 1
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_res = datetime.now() - time_start
print(f'Время выполнения {time_res}')
time_start = datetime.now()
thread1 = Thread(target=write_words, args=(10, 'example1.txt'))
thread2 = Thread(target=write_words, args=(30, 'example2.txt'))
thread3 = Thread(target=write_words, args=(200, 'example3.txt'))
thread4 = Thread(target=write_words, args=(100, 'example4.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
time_res = datetime.now() - time_start
print(f'Время выполнения {time_res}')
