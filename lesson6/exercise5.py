class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Drawing is started for {self.title}')


class Pen(Stationery):
    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print(f'Pen is drawing')


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print(f'Pencil is drawing')


class Handle(Stationery):
    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        print(f'Handle is drawing')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()