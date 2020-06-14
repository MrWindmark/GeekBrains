print("Шестое задание")
print("-"*15)
print("Рассчёт пробежек\n")

def data_input():
    checked = True
    while checked:
        user_ans = input("Укажите значение: ")
        if user_ans.isdigit():
            return user_ans
        else:
            try:
                user_ans = float(user_ans)
                return user_ans
            except ValueError:
                print("Пожалуйста введите число через точку!")

print("Каков результат в первый день?")
first_day_result = float(data_input())
print("Каков желаемый результат?")
target_result = float(data_input())

check_start = True
day_number = 1

while check_start:
    first_day_result = round(first_day_result * 1.1, 2) # это из гугла
    day_number = day_number + 1
    print(f'{day_number}-й день: {first_day_result} км')
    if first_day_result >= target_result:
        print(f"Цель достигается на {day_number}-й день")
        check_start = False