import math
from itertools import repeat


def create_table(size):
    return [x + 1 for x in range(size * size)]


def print_table(table):
    rowsize = math.sqrt(len(table))
    padding = int(math.log10(len(table)) + 1)

    for i, element in enumerate(table):
        print(f"|{element: ^{padding}}", end="")
        if (i + 1) % rowsize == 0:
            print("|")


def add_player_pick(indices, value, player):
    new_object = {key: value for (key, value) in indices.items()}
    new_object[player].append(value)
    new_object[player].sort()
    return new_object


# merge the picks onto the table
def mash_table(indices, game_table):
    picked_indices = [val for listv in indices.values() for val in listv]
    return [get_key(indices, x) if x in picked_indices else x for x in game_table]


def get_key(dict, value):
    for k, vlist in dict.items():
        if value in vlist:
            return k


def swap_player(player):
    return "O" if player == "X" else "X"


def is_incremented_by_one(a, b):
    return a == b - 1


def is_from_same_row(a, b, size):
    return (a - 1) // size == (b - 1) // size


def get_chunks(array, length):
    for i in range(0, len(array), length):
        yield array[i : i + length]


# size = rowlength
def check_for_horizontal(picks, size):
    # counter = 0
    # for index in range(1, len(picks)):
    #     # (2, 3) => 2 == 3-1 and (2-1)//3 == (3-1)//3
    #     if (picks[index - 1] == picks[index] - 1) and (
    #         (picks[index - 1] - 1) // size == (picks[index] - 1) // size
    #     ):
    #         counter += 1
    #     else:
    #         counter = 0
    #     if counter == size - 1:
    #         return True
    # return False

    # # lambda creates a new list, containing 0, 1 values if predicates are false or true respectively.
    # # params: the "picks" list with adjacent values, i.e. picks[i], picks[i+1]
    result = list(
        map(
            lambda tpl: 1
            if is_incremented_by_one(*tpl)
            and is_from_same_row(
                *tpl, size
            )  # variable size is problematic, called out ouf scope
            else 0,
            zip(picks[:-1], picks[1:]),
        )
    )

    chunks = list(get_chunks(result, size - 1))
    return any(total == size - 1 for total in [sum(x) for x in chunks])


def has_winner(picks, size):
    return check_for_horizontal(picks, size)


def initiate_game_variables():
    size = 3
    player = "O"
    indices = {"X": [], "O": []}

    return size, player, indices


if __name__ == "__main__":
    size, player, indices = initiate_game_variables()

    while True:
        player = swap_player(player)
        table = mash_table(indices, create_table(size))
        print_table(table)
        value_chosen = int(input(f"Enter value for player {player}: "))
        indices = add_player_pick(indices, value_chosen, player)
        if has_winner(indices[player], int(math.sqrt(len(table)))):
            print(f"Player {player} has won the game!")
            break
# validate_pick()


# check_for_win()
# # line = 1, 2, 3 (+1)
# # vertical = 1, 4, 7 (+3)
# # diagonal = 1, 5, 9 (+3+1)
# # otherdiagonal = 3,  5, 7 (+2)

# # vertical = 1, 11, 21 (+size)
# # diagonal = 1, 12, 23 (+size +1)
# # otherdiagonal = 10, 19, 28 (+size-1)