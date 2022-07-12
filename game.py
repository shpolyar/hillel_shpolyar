from random import choice


class InputError(Exception):
    pass


class Game:
    _result = {'rock': ['scissors', 'lizard'],
               'paper': ['rock', 'spock'],
               'scissors': ['paper', 'lizard'],
               'lizard': ['paper', 'spock'],
               'spock': ['scissors', 'rock']}

    def __init__(self, player_choice):
        if player_choice in self._result:
            self.player_choice = player_choice
        else:
            raise InputError(f'Invalid input "{player_choice}"')
        self.computer_choice = choice(list(self._result.keys()))

    def fight(self):
        if self.computer_choice in self._result[self.player_choice]:
            print('Player WIN!')
        elif self.player_choice == self.computer_choice:
            print('Draw')
        else:
            print('Computer WIN!')

    @staticmethod
    def repeat():
        answer = input('Repeat (Yes/No)?\n>>> ')
        if answer == 'Yes':
            return True
        elif answer == 'No':
            return False
        else:
            raise InputError(f'Invalid input "{answer}"')


if __name__ == '__main__':
    while True:
        try:
            play = Game(input('Your choice (rock paper scissors lizard spock)?\n>>> '))
        except InputError as e:
            print(e)
            continue
        print(f'Player: {play.player_choice}')
        print(f'Computer: {play.computer_choice}')
        play.fight()
        try:
            if play.repeat():
                continue
            else:
                break
        except InputError as e:
            print(e)
#            не знаю как сделать, чтобы при ошибке снова повторялась функция repeat,
#            пока пользователь не введет правильный ответ
