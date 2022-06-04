import json
import os.path


class Game:
    _previous_move = 'R'
    _num_move = 0
    _back_moves = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}

    def __init__(self, game_map, wrong_moves):
        self._game_map = game_map
        self._wrong_moves = wrong_moves

    def read_savings(self):
        with open('save.json', 'r') as save:
            file_content = save.read()
            templates = json.loads(file_content)
            self._previous_move = templates['previous_move']
            self._num_move = templates['num_move']

    def write_savings(self):
        do_save = input('Зберегтися? Так/Ні: ')
        if do_save == 'Так':
            to_json = {'num_move': self._num_move, 'previous_move': self._previous_move}
            with open('save.json', 'w') as save:
                json.dump(to_json, save)

    def play(self):
        if os.path.isfile('save.json'):
            do_read_saving = input('У вас є збереження. Хочете завантажити? Так/Ні')
            if do_read_saving == 'Так':
                self.read_savings()
            else:
                os.remove('save.json')
        print('''Виберіть хід:
                    R - Вправо
                    L - вліво
                    U - вверз
                    D - вниз
                    E - вихід
                    ''')
        while True:
            print(self._num_move)

            _your_move = input('Ваш хід:').upper()
            if _your_move == 'E':
                print("Вийти та зберегтися")
                self.write_savings()
                break
            if _your_move == self._game_map[self._num_move]:
                self._num_move += 1
                if self._num_move == 24:
                    print('Ура. Ви виграли')
                    break
                self._previous_move = self._game_map[self._num_move]
                print("Правильний хід")
            elif _your_move == self._wrong_moves.get(self._num_move):
                self._previous_move = self._game_map[self._num_move]
                print("Гра закінчена. Ви вибрали невірний шлях")
                self.write_savings()
                break
            elif _your_move == self._back_moves[self._previous_move]:
                print("Гра закінчена. Ви повернулися назад")
                self.write_savings()
                break
            elif _your_move not in self._back_moves:
                print('Неправильний ввід. Спробуйте ще раз')
            else:
                print('Ви вдарилися в стіну.')
                self.write_savings()
                break


game = Game('RDLDRRRRDDRRRRDLDDLDRDRR', {5: 'D', 7: 'U', 8: 'U', 9: 'L', 11: 'D', 17: 'R', 20: 'L'})
game.play()
