print("Четвёртое задание")
print("-"*15)
print("Нахождение наибольшей цифры в числе")

while True:
    user_n = input("Введите целое число больше 0: ")
    if user_n.isdigit():
        user_n = int(user_n)
        if user_n > 0:
            break

user_n = str(user_n)
max_num = '0'
for i in range(0, len(user_n)):
    if user_n[i] > max_num:
        max_num = user_n[i]

print(max_num)