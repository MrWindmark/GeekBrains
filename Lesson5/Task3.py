with open('task3.txt', 'r') as f:
    arrows = f.read().splitlines()

for ln in arrows:
    print(ln)

print('\n' + '-'*20 + '\n')
mid_payment = 0

for itm in arrows:
    data = itm.split(' ')
    if data:
        salary = int(data[1])
        if salary < 20000:
            print(f'Сотрудник: {data[0][:-1]} зарабатывает {salary} рублей')
        mid_payment += salary / len(arrows)

print(f'Средняя з.п.: {round(mid_payment, 2)} рублей')