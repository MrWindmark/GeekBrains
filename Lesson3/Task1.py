def devider(devis, devid):
    try:
        return devis/devid
    except ZeroDivisionError as e:
        return e

def float_reader(name):
    var_r = input(f'Введите {name}:')
    try:
        var_r = float(var_r)
        return var_r
    except ValueError as e:
        print(f'Ошибка {e}. Введите корректное числовое значение')
        return float_reader(name)

var_des = float_reader('делимое')
var_ded = float_reader('делитель')
print(devider(var_des, var_ded))