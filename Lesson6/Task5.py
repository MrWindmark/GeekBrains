class Stationery:
    title = "Магия!"
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'{Stationery.title} Достаём разноцветные ручки и наводим ужас на бумагу')

class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'{Stationery.title} Этот карандаш был украден у Джокера. Он всё ещё функционален')

class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'{Stationery.title} Легенда гласит, что у цветов разный вкус')

test_main = Stationery()
test_main.draw()
print('-'*10)
test_object1 = Pen()
test_object2 = Pencil()
test_object3 = Handle()

test_object1.draw()
print('-'*10)
test_object2.draw()
print('-'*10)
test_object3.draw()

