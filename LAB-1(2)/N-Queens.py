n = int(input("Enter n: "))

a = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    a.append(row)


def check(r, c):

    for i in range(r):
        if a[i][c] == 1:
            return False

    i = r
    j = c
    while i >= 0 and j >= 0:
        if a[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    i = r
    j = c
    while i >= 0 and j < n:
        if a[i][j] == 1:
            return False
        i = i - 1
        j = j + 1

    return True


def queen(r):

    if r == n:
        return True

    for c in range(n):

        if check(r, c):

            a[r][c] = 1

            if queen(r + 1):
                return True

            a[r][c] = 0

    return False


if queen(0):
    for i in range(n):
        print(a[i])
else:
    print("No Solution")