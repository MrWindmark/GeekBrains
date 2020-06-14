print("Второе задание")
print("-"*15)
print("Перевод времени в формат ЧЧ:ММ:СС")

user_time = int(input("Укажите время в секундах: "))

user_hours = user_time//3600
user_time = user_time - user_hours*3600
user_minutes = user_time//60
user_time = user_time - user_minutes*60
user_seconds = user_time

print(f'{user_hours}:{user_minutes}:{user_seconds}')