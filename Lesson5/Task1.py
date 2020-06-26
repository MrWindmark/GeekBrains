end = False

while not end:
    data = input("Enter data: ")
    with open('task1.txt', 'a', encoding='UTF-8') as file:
        file.write(data + '\n')
    if not data:
        end = True
