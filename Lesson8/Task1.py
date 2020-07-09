

class Data:

    def __init__(self, line: str):
        Data.date = line


    @classmethod
    def edit(cls):
        tmp = cls.date.split('-')
        cls.__day = int(tmp[0])
        cls.__month = int(tmp[1])
        cls.__year = int(tmp[2])
        return cls.__day, cls.__month, cls.__year

    @staticmethod
    def date_valid(line):
        tmp = line.split('-')
        day = False
        month = False
        year = False
        if 0 < int(tmp[0]) <= 31:
            day = True
        if 0 < int(tmp[1]) <= 12:
            month = True
        if 1500 < int(tmp[2]) < 2100:
            year = True
        return day * month * year


test = Data('01-02-20')
print(test.edit())
print(test.date_valid('01-02-20'))

test1 = Data('15-07-2020')
print(test1.edit())
print(test1.date_valid('15-07-2020'))

test2 = Data('15-07-1861')
print(test1.edit())
print(test1.date_valid('15-07-1861'))