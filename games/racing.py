from os import system as console
import time as t
import random as rd
from platform import system as sysPlatform


class Player:

    def __init__(self, car, length=5):
        self.__car = car
        self.__length = length
        self.__board = [self.__car] + self.__generate_board()

    def __generate_board(self):
        return ['-' for _ in range(self.__length-1)]

    def getCar(self):
        return self.__car

    def getBoard(self):
        return self.__board


class Table:
    def __init__(self, players: int = 3, length: int = 5, cars: list[int] = ['#', '@', '$']):
        if players > len(cars):
            raise ValueError(
                "Number of players must be less than or equal to number of cars")
        self.__players = [Player(cars[car], length) for car in range(players)]

    def getBoard(self):
        return [player.getBoard() for player in self.__players]

    def __nextMove(self, player: Player):
        board = player.getBoard()
        car = player.getCar()
        carIndex = board.index(car)
        if carIndex >= len(board) or carIndex + 1 >= len(board):
            return True
        return False

    def __move(self, player: Player):
        board = player.getBoard()
        car = player.getCar()
        carIndex = board.index(car)
        if carIndex >= len(board) or carIndex + 1 >= len(board):
            return player
        else:
            board[carIndex] = board[carIndex-1]
            board[carIndex+1] = car
        return None

    def showTable(self):
        for index, player in enumerate(self.__players):
            print(index+1, '[' + ''.join(player.getBoard()) + ']')

    def __clear(self):
        console('cls' if sysPlatform() == 'Windows' else 'clear')

    def __menu(self):
        print('''Welcome to the racing game!\nPress Enter to start the game...
        ''')
        input()

    def __showWin(self, player: Player):
        print(f'Player {player.getCar()} wins!')

    def play(self):
        self.__menu()
        while True:
            self.__clear()
            self.showTable()
            selected = rd.choice(self.__players)
            for player in self.__players:
                if self.__nextMove(player) is not False:
                    self.__showWin(player)
                    return
            result: Player | None = self.__move(selected)
            if result is not None:
                return
            t.sleep(0.01)
