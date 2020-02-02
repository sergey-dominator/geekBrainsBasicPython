
class Warehouse:
    def __init__(self):
        self.equipments = {
            Printer.name: [],
            Scanner.name: [],
            Xerox.name: []
        }

    def add_equipment(self, equipment):
        self.equipments[equipment.name].append(equipment)

    def send_equipment_to_company(self, equipment_name):
        return self.equipments[equipment_name].pop()

    def __str__(self):
        return f"Warehouse contains {len(self.equipments[Printer.name])} of printers, " \
               f"{len(self.equipments[Scanner.name])} of scanners and " \
               f"{len(self.equipments[Xerox.name])} of xeroxes"


class Equipment:
    def __init__(self, name, model):
        self.name = name
        self.model = model


class Printer(Equipment):
    name = "Printer"

    def __init__(self, model):
        super().__init__(self.name, model)


class Scanner(Equipment):
    name = "Scanner"

    def __init__(self, model):
        super().__init__(self.name, model)


class Xerox(Equipment):
    name = "Xerox"

    def __init__(self, model):
        super().__init__(self.name, model)


class WrongAmount(Exception):
    def __init__(self, message):
        self.message = message


warehouse = Warehouse()

while True:
    print("Do you want to (A)dd equipment or to (S)ent equipment to a company?")
    decision = input()

    if decision.lower() == "a":
        print("What do you want to add? (P)rinter, (S)canner or (X)erox?")
        equipment_decision = input()

        print("How many do you want to add?")
        equipment_amount = input()

        try:
            equipment_amount = int(equipment_amount)
            if equipment_amount <= 0:
                raise WrongAmount("You should add at least one equipment")

            for i in range(equipment_amount):
                print(f'Type the model of {i + 1}th equipment: ')
                model = input()
                if equipment_decision.lower() == 'p':
                    warehouse.add_equipment(Printer(model))
                elif equipment_decision.lower() == 's':
                    warehouse.add_equipment(Scanner(model))
                elif equipment_decision.lower() == 'x':
                    warehouse.add_equipment(Xerox(model))
        except ValueError:
            print("You should enter a number")
        except WrongAmount as error:
            print(error.message)

    if decision.lower() == 's':
        print("What do you want to send? (P)rinter, (S)canner or (X)erox?")
        equipment_decision = input()

        print("How many do you want to send?")
        equipment_amount = input()

        try:
            equipment_amount = int(equipment_amount)
            if equipment_amount <= 0:
                raise WrongAmount("You should send at least one equipment")

            for i in range(equipment_amount):
                if equipment_decision.lower() == 'p':
                    if len(warehouse.equipments[Printer.name]) < equipment_amount:
                        raise WrongAmount("Warehouse doesn't have so many equipment")

                    warehouse.send_equipment_to_company(Printer.name)
                elif equipment_decision.lower() == 's':
                    if len(warehouse.equipments[Scanner.name]) < equipment_amount:
                        raise WrongAmount("Warehouse doesn't have so many equipment")

                    warehouse.send_equipment_to_company(Scanner.name)
                elif equipment_decision.lower() == 'x':
                    if len(warehouse.equipments[Xerox.name]) < equipment_amount:
                        raise WrongAmount("Warehouse doesn't have so many equipment")

                    warehouse.send_equipment_to_company(Xerox.name)
        except ValueError:
            print("You should enter a number")
        except WrongAmount as error:
            print(error.message)

    print(warehouse)

    print('Do you want to finish?')
    decision = input()

    if decision.lower() == 'yes':
        break
