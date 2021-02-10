import math


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


def check_for_horizontal(picks, size):
    counter = 0
    for index in range(1, len(picks)):
        # (2, 3) => 2 == 3-1 and (2-1)//3 == (3-1)//3
        if (picks[index - 1] == picks[index] - 1) and (
            (picks[index - 1] - 1) // size == (picks[index] - 1) // size
        ):
            counter += 1
        else:
            counter = 0
        if counter == size - 1:
            return True

    return False


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
        if has_winner(indices[player], math.sqrt(len(table))):
            print(f"Player {player} has won the game!")
            break
# validate_pick()
