with open('test.txt', 'r') as f:
    arrows = f.read().splitlines()

print(f'Общее количество строк в файле: {len(arrows)}')
print('-'*20)

for line in arrows:
    print(line)

print('-'*20)

for idx, itr in enumerate(arrows, 1):
    tmp = itr.split(' ')
    print(f'Строка {idx} включает {len(tmp)} слов(а)')