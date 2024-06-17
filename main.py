def is_valid(board, row, col, num, row_set, col_set, subgrid_set):
    if num in row_set[row] or num in col_set[col] or num in subgrid_set[row // 3][col // 3]:
        return False
    return True

def solve_sudoku(board, row_set, col_set, subgrid_set):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, row, col, i, row_set, col_set, subgrid_set):
            board[row][col] = i
            row_set[row].add(i)
            col_set[col].add(i)
            subgrid_set[row // 3][col // 3].add(i)

            if solve_sudoku(board, row_set, col_set, subgrid_set):
                return True

            board[row][col] = 0
            row_set[row].remove(i)
            col_set[col].remove(i)
            subgrid_set[row // 3][col // 3].remove(i)

    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Initialize the Sudoku board
board = [
    [5, 3, 4, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

row_set = [set() for _ in range(9)]
col_set = [set() for _ in range(9)]
subgrid_set = [[set() for _ in range(3)] for _ in range(3)]

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            num = board[i][j]
            row_set[i].add(num)
            col_set[j].add(num)
            subgrid_set[i // 3][j // 3].add(num)

if solve_sudoku(board, row_set, col_set, subgrid_set):
    print_board(board)
else:
    print("No solution exists")