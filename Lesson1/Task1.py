test_int = 6
test_float = 7.7
test_str = 'Мой любимый день недели? '
test_dict = {'site': 'GeekBrains', 'faculty': 'Python-разработки'}
test_bool = False

while not test_bool:
    prog_start = input('Для начала работы ответьте "Начинаем!": ')
    if prog_start == "Начинаем!":
        test_bool = True

print(f'Домашняя работа для {test_dict["site"]} с факультета {test_dict["faculty"]}')
print("Первое задание")
print("-" * 15)
print(test_str, test_int, '-ой')

# я доверяю пользователю, поэтому не проверяю что введено
print("Десятичная часть указывается через точку")
user_number = input('Введите Ваше любимое число: ')
user_pi = input('Введите число Pi с точностью до 4-х знаков после запятой: ')

try:
    user_number = float(user_number)
    user_pi = float(user_pi)
    # нет, я не полностью доверяю пользователю
    if user_number - user_pi == 0:
        print('Вы математик?')
    elif user_pi == 3.1416:
        print(f'Ваше любимое число {user_number} и вы помните число Pi!')
    else:
        print(f'Вы любите {user_number}, а вот Pi - не помните. Ваш ответ {user_pi}')
except Exception:
    print("А я в тебя верил...")
    print(f'Ваше любимое число {user_number}')
