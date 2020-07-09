
class ListNumError(Exception):
    def __init__(self):
        ListNumError.text = "Not a number position in list. Data erased"

    def err_print(self):
        print(ListNumError.text)

result = []
count = 0
while True:
    tmp = input(f"Enter element {count+1}: ")
    count += 1
    if tmp == 'Stop' or tmp == 'stop':
        print(result)
        break
    try:
        if not tmp.isdigit():
            tmp = ''
            raise ListNumError
        result.append(tmp)
    except ListNumError:
        print(ListNumError.text)