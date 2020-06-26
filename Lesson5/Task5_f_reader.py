with open('task5.txt', 'r', encoding='UTF-8') as file_1:
    data_r = file_1.read().strip().split(' ')

print(f'Прочитано: {data_r}')

sum_res = 0
for i in range(0, len(data_r)):
    sum_res += int(data_r[i])

print(f'Сумма: {sum_res}')
