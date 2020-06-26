import random

numbers = [random.randint(1, 100) for itr in range(0, 15)]
print(f'Создано: {numbers}')

data = ''

for i in range(0, len(numbers)):
    data += str(numbers[i]) + ' '

with open('task5.txt', 'w', encoding='UTF-8') as file:
    file.writelines(data)