def print_params(a=5.5, b='Sample', c=True):
    print(a, b, c)


print_params(a=77, c=[1, 3, 9])
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['77', 77, 77.7]
values_dict = {'a': 70, 'b': 70.7, 'c': '70'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [33.3, 'Rome']
print_params(*values_list_2, 42)
