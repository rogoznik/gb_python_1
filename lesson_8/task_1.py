import random


class Card:
    def __init__(self, name):
        self.name = name
        self.card = list()
        self.generate_card()
        self.count_num_in_card = 15
        self.is_win = False

    def generate_card(self):
        prev_num = list()
        for i in range(3):
            self.card.append(list())
            count_num_in_row = 0
            for j in range(9):
                self.card[i].append(0)

            prev_idx = list()
            while count_num_in_row < 5:
                idx = random.randint(0, 8)

                while idx in prev_idx:
                    idx = random.randint(0, 8)

                m = idx * 10
                n = m + 9 if m != 80 else m + 10
                num = random.randint(m if m > 0 else 1, n)
                prev_idx.append(idx)

                if num not in prev_num:
                    self.card[i].pop(idx)
                    self.card[i].insert(idx, num)
                    count_num_in_row += 1
                    prev_num.append(num)

    def check_num(self, num):
        for row in self.card:
            if row.count(num) > 0:
                idx = row.index(num)
                if idx >= 0:
                    row.pop(idx)
                    row.insert(idx, '-')
                    self.count_num_in_card -= 1
                    break


class Game:
    def __init__(self, player, comp):
        self.players = [player, comp]
        self.print_card()

    def start_game(self):
        is_end_game = False
        prev_num = list()
        count_num = 90

        choice = input('Начать игру? (y/n): ').upper()
        if choice == 'Y':
            while count_num > 0:
                num = random.randint(1, 90)

                while num in prev_num:
                    num = random.randint(1, 90)

                prev_num.append(num)
                count_num -= 1
                print()
                print(f'Новый бочонок: {num} (осталось {count_num})')
                self.print_card()
                choice = input('Зачеркнуть цифру? (y/n): ').upper()

                if choice == 'N':
                    is_end_game = True
                    break

                for plr in self.players:
                    plr.check_num(num)

                for plr in self.players:
                    if plr.count_num_in_card == 0:
                        is_end_game = True
                        plr.is_win = True
                        break

                if is_end_game:
                    break

            if is_end_game:
                print()
                print('Игра окончена')
                self.print_card()
                for plr in self.players:
                    if plr.is_win:
                        print(f'Победил игрок {plr.name}')
                        break

            if count_num <= 0:
                print('Закончились бочонки')

    def print_card(self):
        for plr in self.players:
            print(f'Карточка игрока {plr.name}')
            print('-' * 26)
            print('\n'.join([' '.join(' ' + elem if elem == '-' else str(elem) if elem > 9 else ' ' + str(elem)
                                      if elem > 0 else '  ' for elem in line) for line in plr.card]))
            print('-' * 26)


player = Card('Player')
comp = Card('Comp')
game = Game(player, comp)
game.start_game()
