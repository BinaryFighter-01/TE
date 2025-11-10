# N Queens Problem

def is_safe(board, row, col, n):
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row + 1, col - 1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nq_until(board, col, n):
    # Base case: all queens placed
    if col >= n:
        return True

    # Try placing a queen in each row for this column
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_nq_until(board, col + 1, n):
                return True
            # Backtrack
            board[i][col] = 0
    return False


def solve_nq(n):
    board = [[0] * n for _ in range(n)]
    if not solve_nq_until(board, 0, n):
        print("No Solution.")
        return
    for row in board:
        print(''.join('Q' if x else '.' for x in row))


# Main
solve_nq(4)
