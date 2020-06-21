print('Второе задание')
print('-'*15)
print('Сортировка элементов\n')

# test_list = [1, 'first', 2.5, True, {'key': 'test_value'}, ('name', 'second name', "01.01.1900"), 4.57]

main_list = []
# проверку корректности ввода опускаем
list_len = int(input('Введите число элементов списка: '))
# считаем что список будет заполняться только строками
for num in range(0, list_len):
    main_list.append(input(f'Введите {num+1}-й элемент: '))

for step in range(0, len(main_list), 2):
    temp_list = main_list[step:(step+2)]
    # если в срез будет выходить за пределы, то в нём будет всего 1 элемент и "реверс" ничего не изменит
    main_list[step:step+2] = temp_list[::-1]

print('-'*15)
print("Изначальный список:")
print(f'{main_list}')