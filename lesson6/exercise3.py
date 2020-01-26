class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """
        method return annual salary for current worker
        :return: monthly wage multiplied by 12 months plus annual bonus
        """

        return self._income["wage"] * 12 + self._income["bonus"]


worker = Position("Vasiliy", "Petrov", "Engineer", {"wage": 1000, "bonus": 11000})
print(f'{worker.get_full_name()} has following annual salary: {worker.get_total_income()}')
