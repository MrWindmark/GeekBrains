class Worker:
    def __init__(self, name: str, surname: str, position: str):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income = {"wage": 0, "bonus": 0}

    def income(self, wage: float, bonus: float):
        Worker._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{Worker.name} {Worker.surname} work in position {Worker.position}')

    def get_total_income(self):
        print(f'Income: {Worker._income["wage"] + Worker._income["bonus"]}')


new = Position('Mike', 'Wazovski', 'Cardinal')
new.income(15000, 45250)

print(type(new))

new.get_full_name()
new.get_total_income()
