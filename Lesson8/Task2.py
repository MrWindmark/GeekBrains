class ZeroDev(Exception):
    def __init__(self):
        ZeroDev.text = 'Zero Division Error!'

    def zero_dev():
        print(ZeroDev.text)
        return float('inf')


urs_divr = float(input("Enter divider: "))
usr_divd = float(input("Enter dividend: "))

try:
    if urs_divr == 0:
        raise ZeroDev
    result = usr_divd / urs_divr
except ZeroDev as e:
    result = ZeroDev.zero_dev()

print(result)
print(type(result))