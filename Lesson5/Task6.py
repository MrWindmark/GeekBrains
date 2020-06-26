with open('Task6.txt', 'r') as file:
    data = file.read().split('\n')

res_dict = {}
les_name = []
r_les_time = []

for itm in data:
    tmp = itm.split(':')
    les_name.append(tmp[0])
    r_les_time.append(tmp[1].split(' '))
# здесь удаляем пустую строку и преобразуем элементы в числа
for itm in r_les_time:
    itm.pop(0)
    for i in range(0, 3):
        if itm[i] != '—':
            itm[i] = int(itm[i])

sum_time = []

for itm in r_les_time:
    tmp = 0
    for i in range(0, 3):
        if itm[i] != '—':
            tmp += itm[i]
    sum_time.append(tmp)

for i in range(0, len(les_name)):
    res_dict[les_name[i]] = sum_time[i]

print(res_dict)
