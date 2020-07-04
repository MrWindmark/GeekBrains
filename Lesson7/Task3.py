
class OrganicCell:
    def __init__(self, cell_num):
        self.__cell_num = cell_num

    @property
    def cell_num(self):
        return self.__cell_num

    def __add__(self, other):
        return OrganicCell(self.cell_num + other.cell_num)


    def __sub__(self, other):
        if self.cell_num > other.cell_num:
            return OrganicCell(self.cell_num - other.cell_num)
        else:
            print("Operation can't be complete")

    def __mul__(self, other):
        return OrganicCell(self.cell_num * other.cell_num)

    def __truediv__(self, other):
        return OrganicCell(self.cell_num // other.cell_num)

    def make_order(self, num_in_line):
        # я пытался здесь использовать генератор, но ничего не вышло
        full_line = self.cell_num // num_in_line
        cutted_line = self.cell_num % num_in_line
        result = ''
        for itr in range(full_line):
            result += '*' * num_in_line + '\n'
        result += '*' * cutted_line + '\n'
        print(result)
        # всё же мне ближе метод работы а-ля C++, со временем отвыкну


cell1 = OrganicCell(7)
cell2 = OrganicCell(6)

cell3 = cell1 + cell2 # 13 клеток
cell3.make_order(5)

cell4 = cell3 - cell1 # 6 клеток
cell4.make_order(5)

cell5 = OrganicCell(2)
cell6 = cell5 * cell2 # 12 клеток
cell6.make_order(5)