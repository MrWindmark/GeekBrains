test_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
test_list2 = [12, 22, 8, 9, 62, 41, 14, 41, 6, 9, 12, 7, 22, 11]

# уникальность значения проверяется методом list.count()
result_list = [step for step in test_list if test_list.count(step) == 1]
print(result_list)
result_list = [step for step in test_list2 if test_list2.count(step) == 1]
print(result_list)