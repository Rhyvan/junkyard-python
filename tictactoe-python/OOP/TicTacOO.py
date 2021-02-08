import math
from collections import deque
import Util

############### Class TABLE ###############
class Table:
    def __init__(self, size):
        self.size = size
        self.data = [[x * size + y for y in range(1, size + 1)] for x in range(size)]
        # digits of max cell value
        self.padding = int(math.log10(size * size) + 1)

    def print_table(self):
        for row in self.data:
            print("|", end="")
            for element in row:
                print(f"{element:^{self.padding}}|", end="")
            print()


############### class GAME ###############
class Game:

    is_game_over = False
    current_player = "O"

    def __init__(self, table_size, winning_size):
        self.table = Table(table_size)
        self.winning_size = winning_size
        self.input_handler = InputHandler()

    def __check_for_winner(self, row, column):
        q = Util.Util.generate_queue(row, column)
        tracker = Util.Util.get_tracker()
        while len(q) > 0:
            curr = q.popleft()
            if curr.isTrue(self.table.data, self.current_player):
                curr.increment_i()
                tracker[curr.index] += 1
                q.append(curr)

        return any(x >= self.winning_size for x in tracker)

    def __change_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_turn(self):
        self.__change_player()
        row, column = self.input_handler.get_user_input(self.current_player, self.table)

        self.table.data[row][column] = self.current_player
        self.is_game_over = self.__check_for_winner(row, column)


###############  class INPUTHANDLER ###############
class InputHandler:
    def get_user_input(self, current_player, table):
        while True:
            try:
                # this text about turn should be here or in an upper level?
                pick = int(input(f"player {current_player}'s turn: ")) - 1
            except ValueError:
                print("please input a natural number")
            else:
                row, column = pick // table.size, pick % table.size
                if self.__validate_pick__(row, column, table):
                    break
                print("invalid number")

        return row, column

    def __validate_pick__(self, row, column, table):
        if row < 0 or row >= table.size:
            return False
        if column < 0 or column >= table.size:
            return False

        return type(table.data[row][column]) is int


###############  MAIN ###############
if __name__ == "__main__":
    table_size = int(input("please add the size of the table: "))
    winning_size = int(input("please add the size of consecutive winning symbols: "))
    game = Game(table_size, winning_size)

    while True:
        game.table.print_table()
        game.play_turn()
        if game.is_game_over:
            break

    print(f"{game.current_player} has won the game!")