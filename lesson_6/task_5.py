class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('пишем')


class Pencil(Stationery):
    def draw(self):
        print('рисуем')


class Handle(Stationery):
    def draw(self):
        print('выделяем')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
