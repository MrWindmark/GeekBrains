def my_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)

val_1 = 156
val_2 = 154
val_3 = 115

print(my_func(val_1, val_2, val_3))
print(my_func(4, 8, 6))