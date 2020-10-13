class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {
        'wage': 0,
        'bonus': 0
    }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def set_income(self, wage, bonus):
        self._income.update({'wage': wage, 'bonus': bonus})


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + (self._income['wage'] * self._income['bonus'])


position = Position('Ivan', 'Ivanov', 'master')
position.set_income(10000, 0.15)

print('Name:', position.get_full_name())
print('Total income:', position.get_total_income())
