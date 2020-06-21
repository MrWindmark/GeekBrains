def user_print(name: list, surname: list, year_of_brth: list, liv_city: list, email: list, phone_number: list):
    return f'ФИО: {name} {surname}. Год рождения: {year_of_brth}. Проживает: {liv_city}. Контакты: {email}, {phone_number}'


name = 'Иван'
surnn = 'Примерный'
birth = '1966'
city = 'Припять'
email = 'stalker@tikuda.ru'
phn_number = '8-800-555-35-35'

print(user_print(surname=surnn, liv_city=city, email=email, phone_number=phn_number, name=name, year_of_brth=birth))

user_data_2 = {
    'surname': 'Примерный',
    'name': 'Иван',
    'liv_city': 'Припять',
    'email': 'stalker@tikuda.ru',
    'phone_number': '8-800-555-35-35',
    'year_of_brth': '1966'
}

print(user_print(**user_data_2))
