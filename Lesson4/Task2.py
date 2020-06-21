test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
test_list2 = [4, 7, 16, 84, 71, 0, 1, 1, 3, 19, 17, 21, 13]

# я думаю что перемудрил здесь
# запускаем цикл до предпоследнего значения. Текущее сравниваем со следующим
# если следующее больше текущего - добавляем его в результат
result_list = [test_list[i + 1] for i in range(0, len(test_list) - 1) if test_list[i + 1] > test_list[i]]
result_list2 = [test_list2[i + 1] for i in range(0, len(test_list2) - 1) if test_list2[i + 1] > test_list2[i]]

print(result_list)
print(result_list2)
