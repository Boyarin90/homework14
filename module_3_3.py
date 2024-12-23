def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2, 'оптимус', False)
print_params(3, 'прайм')
print_params(a= 'с', b= 'новым', c= 'годом')
print_params(a= 'год', b= 'змеи')
print_params(b= 'новый', c= 'год')
print_params(b= 25)
print_params(c= [1, 2, 3])

values_list = ['c наступающим', 2025, True]
values_dict = {'a': 'новый', "b": 2025, 'c': 0.9}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["Поздравляю Вас с наступающим новым годом", 2025]

print_params(*values_list_2, 42)

