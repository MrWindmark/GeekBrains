def my_func(a: float, b: int):
    if b < 0 < a:
        return a ** b
    else:
        return 0


def cyc_my_func(a: float, b: int):
    if b < 0 < a:
        l_sum = 1
        for step in range(abs(b)):
            l_sum *= a
        return 1 / l_sum
    elif b == 0 < a:
        return 1
    else:
        raise ValueError("Не отрицательная степень")


print(my_func(10.5, -3))
print("-" * 30)
print(cyc_my_func(10.5, 3))
