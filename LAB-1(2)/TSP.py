from itertools import permutations

n = int(input("Enter number of cities: "))

a = []

print("Enter the cost matrix:")

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

city = []

for i in range(1, n):
    city.append(i)

ans = 99999

for p in permutations(city):

    cost = 0
    k = 0

    for i in p:
        cost = cost + a[k][i]
        k = i

    cost = cost + a[k][0]

    if cost < ans:
        ans = cost

print("Minimum Cost =", ans)