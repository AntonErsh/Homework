calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    if string in list_to_search:
        return True
    else:
        return False


print(string_info('Alyoooo'))
print(is_contains('PeGeOn', ['Peg', 'Peugeit', 'Pegeon']))
print(string_info('Ratatata'))
print(is_contains('KulmBacher', ['Bax', 'Jigit', 'Karely']))
print(calls)
