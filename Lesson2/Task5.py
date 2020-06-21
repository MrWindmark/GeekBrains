print('Пятое задание')
print('-'*15)
print('Структура "Рейтинг"\n')

exit_chk = True
test_list = [11, 9, 7, 7, 4, 3]
tmp_list = []

print("Для выхода введите 'Exit'\n")

while exit_chk:
    new_elem = input("Укажите новый элемент рейтинга: ")
    if new_elem != 'Exit':
        new_elem = int(new_elem)
    else:
        exit_chk = False
    for i in range(0, len(test_list)):
        if test_list[-1] >= new_elem:
            test_list.append(new_elem)
            break
        elif test_list[i] < new_elem:
            tmp_list = test_list[i:]
            tmp_list = tmp_list[::-1]
            tmp_list.append(new_elem)
            test_list[i:] = tmp_list[::-1]
            break
    print(test_list)