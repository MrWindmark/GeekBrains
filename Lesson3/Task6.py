def int_func(string: str):
    if string.isalpha():
        # print("We are here")
        return string.capitalize()
    elif string.lower():
        # print("And now we are here")
        return string.title()


print(int_func('walk'))
print('-' * 10)
print(int_func('hello my dear friend!'))
print('-' * 10)
print(int_func('hello my dear 11 friend!'))
