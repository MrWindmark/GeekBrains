with open('task4.txt', 'r') as f:
    arrows = f.read().splitlines()

print(arrows)
define = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
result = []

for itm in arrows:
    tmp = itm.split(' — ')
    buff = define[tmp[0]] + ' — ' + tmp[1]
    result.append(buff)

for itm in result:
    with open('task4_result.txt', 'a', encoding='UTF-8') as file:
        file.write(itm + '\n')