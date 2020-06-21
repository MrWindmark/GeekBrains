from sys import argv

# первым параметром идёт адрес файла со скриптом, его записываем в мусор через _
_, work_time, pay_for_hour, addition = argv

print(f'При {work_time} рабочих часах по ставке {pay_for_hour}, с учётом премии в {addition}')
result_payment = float(work_time)*float(pay_for_hour) + float(addition)
print(f'Зарплата {result_payment}')