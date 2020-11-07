import os
import random
import time


def clean_console():
    os.system("cls || clear")


def set_board_size():
    column_length = input("Please enter number of rows in the board: \n")
    acceptable_column_sizes = [4, 6, 10]
    while not column_length.isdigit() or int(column_length) not in acceptable_column_sizes:
        column_length = input(f"Wrong input! Please choose a number from {acceptable_column_sizes}.\n"
                              f"Number of rows in the board: \n")
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
    print()


def board_not_empty(board):
    for row in board:
        for mark in row:
            if mark == "#":
                return True
    return False


def place_is_empty(row, column, board):
    return board[row][column] == "#"


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
    return board


def get_input(column_length):
    columns_labels = ["A", "B", "C", "D", "E"]

    coordinate = input("Please provide coordinate: \n ").upper()
    while len(coordinate) != 2 or \
            (not coordinate[0].isalpha() or coordinate[0] not in columns_labels) or \
            (not coordinate[1].isdigit() or int(coordinate[1]) > column_length):
        coordinate = input("Wrong input, please provide correct coordinate: \n ").upper()
    return coordinate


def coordinates_translation(coordinate):
    columns_labels = ["A", "B", "C", "D", "E"]
    col_index = columns_labels.index(coordinate[0])
    row_index = int(coordinate[1]) - 1
    return row_index, col_index


def ensure_correct_input(board_size, board):
    row, column = coordinates_translation(get_input(board_size))
    while not place_is_empty(row, column, board):
        print("This spot is taken. Please enter coordinate again!")
        row, column = coordinates_translation(get_input(board_size))
    return row, column


def main():
    board_size = set_board_size()
    visible_board = init_board(board_size)
    symbols = get_symbols(board_size)
    hidden_board_empty = init_board(board_size)
    hidden_board = populate_bord_with_symbols(hidden_board_empty, symbols)
    print(hidden_board)
    while board_not_empty(visible_board):
        clean_console()
        print_board(visible_board)
        x1, y1 = ensure_correct_input(board_size, visible_board)
        visible_board[x1][y1] = hidden_board[x1][y1]
        print_board(visible_board)
        x2, y2 = ensure_correct_input(board_size, visible_board)
        visible_board[x2][y2] = hidden_board[x2][y2]
        if visible_board[x1][y1] != visible_board[x2][y2]:
            print_board(visible_board)
            time.sleep(2.0)
            visible_board[x1][y1] = visible_board[x2][y2] = "#"
            clean_console()
    print("You have won!")


if __name__ == '__main__':

    print("Welcome to memory game!\n")
    main()
