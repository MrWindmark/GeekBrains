print('Шестое задание')
print('-'*15)
print('Структура "Товары"\n')

goods_list = [
    (1, {'name': "компьютер", 'price': 35000, 'pieces': 9, 'unit': "шт."}),
    (2, {'name': "принтер", 'price': 7000, 'pieces': 7, 'unit': "шт."}),
    (3, {'name': "сканер", 'price': 6500, 'pieces': 3, 'unit': "шт."}),
    (4, {'name': "дисплей", 'price': 9500, 'pieces': 7, 'unit': "шт."})
    ]

def add_goods(goods_list):
    goods = {'name':'', 'price':'', 'pieces':'', 'unit':''}
    goods['name'] = input("Укажите наименование товара: ")
    goods['price'] = input("Укажите стоимость товара: ")
    goods['pieces'] = input("Укажите количество товара: ")
    goods['unit'] = input("Укажите единицу измерения числа товара: ")
    goods_list.append((len(goods_list)+1, goods))

def goods_analysys(goods_list, check_key):
    result_list = []
    for step in goods_list:
        result_list.append(step[1].get(check_key))
    return result_list

print("Используйте следующее меню:")
print("1 - Для добавления элемента")
print("2 - Для фильтр данных")
print("3 - Для завершения работы")

is_it_work = True
# goods_list = []

while is_it_work:
    print("-" * 20)
    menu_val = input("Желаемое действие: ")
    print("-" * 20)
    if menu_val == '1':
        add_goods(goods_list)
    elif menu_val == '2':
        print('Доступные параметры для фильтрации:\n\t1 - наименование,\n\t2 - стоимость,\n\t3 - количество,\n\t4 - единица измерения')
        keys_num = int(input("Укажитие желаемый пункт для фильтрации: "))
        check_key = list(goods_list[0][1].keys())
        filtered_list = goods_analysys(goods_list, check_key[keys_num-1])
        print(filtered_list)
    elif menu_val == '3':
        is_it_work = False
        print("Досвидания")
    else:
        print("-"*20)
        print("Ошибка, повторите ввод")
        print("-" * 20)

