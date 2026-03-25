import numpy as np

def generate_sudoku_board():
    rng = np.random.default_rng()

    # Start with simple valid board
    board = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [2, 3, 1, 5, 6, 4, 8, 9, 7],
                      [5, 6, 4, 8, 9, 7, 2, 3, 1],
                      [8, 9, 7, 2, 3, 1, 5, 6, 4],
                      [3, 1, 2, 6, 4, 5, 9, 7, 8],
                      [6, 4, 5, 9, 7, 8, 3, 1, 2],
                      [9, 7, 8, 3, 1, 2, 6, 4, 5]], dtype=int)
    
    # Shuffle all digits
    new_digits = np.arange(1, 10)
    rng.shuffle(new_digits)
    
    for i in range(9):
        mask1 = (board == i+1)
        mask2 = (board == new_digits[i])

        temp = board[mask2].copy()
        board[mask2] = i+1
        board[mask1] = new_digits[i]

    # Rearrange collumns 1, 2 and 3 with themselves
    # Then rearrange collumns 4, 5 and 6 with themselves
    # Then rearrange collumns 7, 8 and 9 with themselves
    for i in range(3):
        col = np.arange(0, 3)
        for n in range(3):
            col[n] = col[n] + 3*i
        sub_board = board[:, col]
        rng.shuffle(sub_board.T)
        board[:, col] = sub_board

    # Rearrange rows 1, 2 and 3 with themselves
    # Then rearrange rows 4, 5 and 6 with themselves
    # Then rearrange rows 7, 8 and 9 with themselves
    for i in range(3):
        row = np.arange(0, 3)
        for n in range(3):
            row[n] = row[n] + 3*i
        sub_board = board[:, row]
        rng.shuffle(sub_board)
        board[:, row] = sub_board
    
    # Rearrange 3 collumn groups of size 9x3
    col_groups = np.arange(3)
    rng.shuffle(col_groups)
    col_order = np.concatenate([np.arange(3 * g, 3 * g + 3) for g in col_groups])
    board = board[:, col_order]
    
    # Rearrange 3 row groups of size 3x9
    row_groups = np.arange(3)
    rng.shuffle(row_groups)
    row_order = np.concatenate([np.arange(3 * g, 3 * g + 3) for g in row_groups])
    board = board[row_order, :]
    
    return board

board = generate_sudoku_board()
print(board)
print(board[1][2])