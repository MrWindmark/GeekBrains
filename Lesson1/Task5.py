print("Пятое задание")
print("-"*15)
print("Рассчёт издержек\n")

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
                print("Пожалуйста введите число!")


print("Укажите выручку компании за год")
income = float(data_input())
print("Укажите издержки компании за год")
costs = float(data_input())

print(f'Прибыль = {income} и издержки = {costs}')


if income > costs:
    print(f'\nФирма отработала с прибылью {income-costs}')
    print(f"Рентабельноесть {(income-costs)/income}")
elif income == costs:
    print("\nФирма не терпит убытков, но и прибыль не принесла")
else:
    print(f'\nФирма отработала с убытком {costs-income}')

print("Укажите число сотрудников в компании")
employee_num = float(data_input())
print(f"Прибыль на сотрудника = {(income-costs)/employee_num}")

