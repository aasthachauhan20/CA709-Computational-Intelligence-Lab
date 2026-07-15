graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

visited = []


def euler(v):

    while graph[v]:

        u = graph[v].pop()

        graph[u].remove(v)

        euler(u)

    visited.append(v)


euler(0)

print("Euler Path:")

print(visited[::-1])