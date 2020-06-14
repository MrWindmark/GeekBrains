print('Первое задание')
print('-'*15)
print('Работа со списками\n')

test_list = [1, 'first', True, 2.5, {'key': 'test_value'}, ('name', 'second name', "01.01.1900")]

print(test_list)
for step in test_list:
    print(f'Тип: {type(step)} для значения \"{step}\"')