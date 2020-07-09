class OffEquipStorage:
    storage = []

    def __init__(self, storage_number):
        self.st_num = storage_number

    def add_obj(self, storage_number):
        self.storage += {'Storage': storage_number}

    def prt(self):
        print(self.storage)

# нужен список списков
class OffEquip(OffEquipStorage):
    def __init__(self, storage_number: int, name: str, amount: int):
        super().__init__(storage_number)
        self.data = {'Name': name, 'Amount': amount}

    def add_obj(cls):
        OffEquipStorage.storage += cls.data


class Printer(OffEquip):
    def __init__(self, storage_number: int, name: str, amount: int, subs_branch: str):
        super().__init__(storage_number, name, amount)
        self.data = {'Storage': storage_number, 'Name': name, 'Amount': amount, 'Type': 'Printer',
                     'Branch': subs_branch}

    def add_obj(self, storage_number: int, name: str, amount: int, subs_branch: str):
        self.storage += {'Storage': storage_number, 'Name': name, 'Amount': amount, 'Type': 'Printer',
                             'Branch': subs_branch}


class Scanner(OffEquip):
    def __init__(self, storage_number: int, name: str, amount: int, subs_branch: str):
        super().__init__(storage_number, name, amount)
        self.data = {'Storage': storage_number, 'Name': name, 'Amount': amount, 'Type': 'Scanner',
                     'Branch': subs_branch}

    def add_obj(self, storage_number: int, name: str, amount: int, subs_branch: str):
        tmp_data = {'Storage': storage_number, 'Name': name, 'Amount': amount, 'Type': 'Scanner', 'Branch': subs_branch}
        self.storage += tmp_data


class CopyMachine(OffEquip):
    def __init__(self, storage_number: int, name: str, amount: int, subs_branch: str):
        super().__init__(storage_number, name, amount)
        self.data = {'Storage': storage_number, 'Name': name, 'Amount': amount, 'Type': 'CopyMachine',
                     'Branch': subs_branch}

    def add_obj(self, storage_number: int, name: str, amount: int, subs_branch: str):
        self.storage += {'Storage': storage_number, 'Name': name, 'Amount': amount, 'Type': 'CopyMachine',
                             'Branch': subs_branch}


test = OffEquip(4, 'Name', 2)
print(test.st_num)
print(test.data)
test.add_obj(test)

print('-' * 5)
test1 = Printer(5, 'Canon', 4, 'Msk')
# test1.add_pos(test1)
# print(test1.st_num, test1.name, test1.amount, test1.type, test1.branch)
print(test1.st_num)
print(test1.data)
test1.add_obj(5, 'Canon', 4, 'Msk')

print('-' * 5)
test2 = Scanner(3, 'HP', 10, 'Spb')
# print(test2.st_num, test2.name, test2.amount, test2.type, test2.branch)
print(test2.st_num)
print(test2.data)
test2.add_obj(3, 'HP', 10, 'Spb')

print('-' * 5)
test3 = CopyMachine(5, 'Xerox', 3, 'Main')
# print(test3.st_num, test3.name, test3.amount, test3.type, test3.branch)
print(test3.st_num)
print(test3.data)
test3.add_obj(5, 'Xerox', 3, 'Main')

print('-'*100)
print(OffEquipStorage.storage)

