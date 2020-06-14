print("Третье задание")
print("-"*15)
print("Ищем сумму n + nn + nnn")

while True:
    user_n = input("Введите целое число: ")
    if user_n.isdigit():
        user_n = int(user_n)
        break

user_nn = str(user_n)*2
user_nnn = str(user_n)*3
n_summ = user_n + int(user_nn) + int(user_nnn)
print(f'Сумма {user_n} + {user_nn} + {user_nnn} равна: {n_summ}')