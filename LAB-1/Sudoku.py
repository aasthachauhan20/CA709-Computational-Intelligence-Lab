import random
board = []

for i in range(9):
    row = []
    for j in range(9):
        row.append(0)
    board.append(row)


# Function to print the board
def print_board():

    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


# check safe
def is_safe(row, col, num):

   
    for j in range(9):
        if board[row][j] == num:  #row
            return False

    for i in range(9):
        if board[i][col] == num:   #col
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3     #3*3 box

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def generate():

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                numbers = [1,2,3,4,5,6,7,8,9]
                random.shuffle(numbers)

                for num in numbers:

                    if is_safe(row, col, num):

                        board[row][col] = num

                        if generate():
                            return True

                        # backtrack
                        board[row][col] = 0

                return False

    return True


#  Sudoku
generate()

print("Generated Sudoku:\n")
print_board()