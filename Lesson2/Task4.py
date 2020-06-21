print('Четвёртое задание')
print('-'*15)
print('Работа с разделением строк\n')

# test_list = 'First Second Third and etc.'

main_arr = input("Введите вашу строку: ")

print('-'*15)
for step in main_arr.split(' '):
    print(f'{step[0:10]}')