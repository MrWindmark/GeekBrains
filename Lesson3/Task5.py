def sum_arr(line: list):
    result = []
    for step in line:
        val_1 = step
        if val_1.isdigit():
            result.append(int(val_1))
        elif val_1 == '!':
            return result
        else:
            raise ValueError
    return result


def summ_er(val_list):
    result = 0
    for step in val_list:
        result += step
    return result


main_sum = 0

while True:
    print("Для остановки введите '!'")
    read_list = input("Введите строку чисел разделённых пробелами: ")
    read_list = read_list.split(' ')
    try:
        test = sum_arr(read_list)
        main_sum += summ_er(test)
    except ValueError:
        print("Ошибка, введите строку чисел!")
    print(f'Общая сумма: {main_sum}')