N = int(input("Enter value of N: "))

board = [[0] * N for i in range(N)]


def is_safe(row, col):

    #  left side of row
    for j in range(col):
        if board[row][j] == 1:
            return False

    #  upper-left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    #  lower-left diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(col):

    if col == N:
        return True

    for row in range(N):

        if is_safe(row, col):

            board[row][col] = 1

            if solve(col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


solve(0)

print("\nSolution:\n")

for row in board:
    print(row)