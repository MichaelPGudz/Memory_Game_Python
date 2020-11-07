def set_board_size():
    row_length = input("Please enter number of rows in the board: \n")
    acceptable_column_sizes = [4, 6, 10]
    while not row_length.isdigit() or int(row_length) not in acceptable_column_sizes:
        row_length = input("Please enter number of rows in the board: \n")
    return int(row_length)


def init_board(row_length):
    column_length = 5
    board = []
    row = []
    while len(row) < row_length:
        row.append("X")
    while len(board) < column_length:
        copy_row = row.copy()
        board.append(copy_row)
    return board

def print_board(board_state):
    columns_labels = ["A", "B", "C", "D", "E"]
    
    print("  " +"columns_labels")

    for index, row in enumerate(board_state, 1):
        print(f"{index}", end="")
        for i in range(len(columns_labels)):
            print(board_state[index][i], end="")
        print()




if __name__ == '__main__':
    board_size = set_board_size()
    board = init_board(board_size)
    print_board(board)