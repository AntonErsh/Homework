def custom_write(file_name: str, strings: list) -> dict:
    write_file = open(file_name, 'w', encoding='UTF-8')
    strings_position = {}
    count = 1
    for i in strings:
        key_dict = (count, write_file.tell())
        strings_position.update({key_dict: i})
        write_file.write(f'{i}\n')
        count += 1
    write_file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
