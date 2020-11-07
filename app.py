import random
from copy import deepcopy


def set_board_size():
    column_length = input("Please enter number of rows in the board: \n")
    acceptable_column_sizes = [4, 6, 10]
    while not column_length.isdigit() or int(column_length) not in acceptable_column_sizes:
        column_length = input("Please enter number of rows in the board: \n")
    return int(column_length)


def init_board(column_length):
    row_length = 5
    board = []
    row = []
    while len(row) < row_length:
        row.append("#")
    while len(board) < column_length:
        copy_row = row.copy()
        board.append(copy_row)
    return board


def print_board(board_state):
    columns_labels = ["A", "B", "C", "D", "E"]
    print("  ", end=" ")
    for label in columns_labels:
        print(label, end=" ")
    print()
    for index, row in enumerate(board_state, 1):
        if index >= 10:
            print(f"{index}", end=" ")
        else:
            print(f" {index}", end=" ")
        for i in range(len(columns_labels)):
            print(board_state[index-1][i], end=" ")
        print()


def get_symbols(col_length):
    allowed_characters = []
    for character in range(225, (225 + int(col_length * 5/2))):
        allowed_characters.append(chr(character))
    return allowed_characters


def populate_bord_with_symbols(board, symbols):
    while len(symbols) > 0:
        symbol = random.choice(symbols)
        symbols.remove(symbol)
        counter = 0
        while counter < 2:
            row = random.randint(0, len(board)-1)
            column = random.randint(0, len(board[row])-1)
            if board[row][column] == "#":
                board[row][column] = symbol
                counter += 1
    populated_board = deepcopy(board)
    return populated_board

def get_input():
    while True:
        coords = input("Please provide coordinates: \n ").upper()
        if len(coords) != 2 or not coords[1].isdigit() or not coords[0].isalpha():
            coords = input("Wrong input, please provide available coordinates: \n ").upper()
        return coords


def coords_translation(coords):
    columns_labels = ["A", "B", "C", "D", "E"]
    col_index = columns_labels.index(coords[0])
    row_index = int(coords[1]) - 1
    return row_index, col_index


def board_not_empty(board):
    for row in board:
        for mark in row:
            if mark == "#":
                return True
    return False



def main():
    board_size = set_board_size()
    display_board = init_board(board_size)
    print_board(display_board)
    gettin_symbols = get_symbols(board_size)
    hidden_board = populate_bord_with_symbols(display_board, gettin_symbols)

    while board_not_empty(display_board):
        coord1, coord2 = coords_translation(get_input())
        display_board[coord1][coord2] = hidden_board[coord1][coord2]
        print_board(display_board)
        coord3, coord4 = coords_translation(get_input())

        
if __name__ == '__main__':
    main()