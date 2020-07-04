from copy import deepcopy

class Matrix:
    def __init__(self, matrix: list):
        self.matrix = deepcopy(matrix)

    # подсмотрено в интернете, в принципе, тут просто формирование строки с форматированием данных табуляцией
    # естественно с помощью генератора строк
    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    # а можно и так
    def matrix_print(self):
        for row in self.matrix:
            print('\t'.join(map(str, row)))

    # тут я вспоминал как работа с матрицами реализовывалась в С++
    def elem_creation(self, r_size: int, c_size: int):
        line_of_lines = []
        for row in range(r_size):
            user_row = []
            for column in range(c_size):
                tmp = float(input(f'Enter element [{row}][{column}]: '))
                user_row.append(tmp)
            line_of_lines.append(user_row)
        return Matrix(line_of_lines)

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        # объявляем второй объект класса
        result = Matrix(other)
        # мезонский балет как при создании объекта
        line_of_lines = []
        for row in range(len(self.matrix)):
            user_row = []
            for column in range(len(self.matrix[row])):
                # для перемещения по объекту Matrix нужен __getitem__
                # я потратил на осознание этого чёртовы 50 минут своей жизни
                tmp = result[row][column] + self.matrix[row][column]
                user_row.append(tmp)
            line_of_lines.append(user_row)
        # создаём новый объект из полученных данных
        return Matrix(line_of_lines)


row_size = int(input('Enter matrix row size: '))
column_size = int(input('Enter matrix column size: '))
test1 = Matrix.elem_creation(Matrix, row_size, column_size)
print('-' * 10)
test1.matrix_print()
print('-' * 10)
print(str(test1))

lines1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
lines2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
test2 = Matrix(lines1)
test3 = Matrix(lines2)
# print('-' * 10)
# test2.matrix_print()
print('-' * 10)
print('Суммируем')
test4 = test2 + test3
print(str(test2))
print('\n')
print(str(test3))
print('-' * 10)
# test3.matrix_print()

print('Результат')

test4.matrix_print()
