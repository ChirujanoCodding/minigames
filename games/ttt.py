import os
from random import randint
class Game:

    def __init__(self, data:dict ={
        'players': ['X','O'],
        'Nicks': ['Player 1','Player 2']
    }):
        self.__data = data
        self.__board = self.__generate_board()

    def __clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __generate_board(self):
        return [[str(i*3+j+1) for j in range(3)] for i in range(3)]

    def __print_board(self):
        for i, v in enumerate(self.__board):
            print(' | '.join(v).center(20))
            if i != 2:
                print('-'*20)


    def __eval(self):
        if self.__board[0][0] == self.__board[0][1] == self.__board[0][2]:
            return 'Winner'
        if self.__board[1][0] == self.__board[1][1] == self.__board[1][2]:
            return 'Winner'
        if self.__board[2][0] == self.__board[2][1] == self.__board[2][2]:
            return 'Winner'
        if self.__board[0][0] == self.__board[1][0] == self.__board[2][0]:
            return 'Winner'
        if self.__board[0][1] == self.__board[1][1] == self.__board[2][1]:
            return 'Winner'
        if self.__board[0][2] == self.__board[1][2] == self.__board[2][2]:
            return 'Winner'
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2]:
            return 'Winner'
        if self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
            return 'Winner'
        return False


    def play(self):
        round = randint(1,2)
        while True:
            self.__clear()
            self.__print_board()
            print(f'{self.__data["Nicks"][round%2]} turn ( {self.__data["players"][round%2]} )')
            try:
                pl = int(input('Enter the position: '.center(20)) ) - 1
            except ValueError:
                continue
            if pl < 0 or pl > 8:
                print('Invalid position')
                input('Press enter to continue...'.center(20))
                continue
            if self.__board[pl//3][pl%3] != self.__data['players'][0] and self.__board[pl//3][pl%3] != self.__data['players'][1]:
                self.__board[pl//3][pl%3] = self.__data['players'][round%2]
                round += 1
            else:
                print('Invalid position (Another put there)'.center(20))
                input('Press enter to continue...'.center(20))
                continue

            if self.__eval():
                self.__clear()
                self.__print_board()
                print(f'{self.__data["Nicks"][round%2]} win!'.center(20))
                break
            if round > 9 and self.__eval() == False:
                self.__clear()
                self.__print_board()
                print('Draw!'.center(20))
                break



        
