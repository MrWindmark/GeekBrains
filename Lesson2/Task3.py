print('Третье задание')
print('-'*15)
print('Работа с месяцами\n')

dict_month_season = {'12':'Зима','1':'Зима','2':'Зима','3':'Весна','4':'Весна','5':'Весна','6':'Лето','7':'Лето','8':'Лето','9':'Осень','10':'Осень','11':'Осень'}
list_month_seasom = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]

month = input("Укажите номер месяца: ")


print(dict_month_season.get(month))
print(list_month_seasom[int(month)-1])