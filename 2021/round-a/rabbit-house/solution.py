from collections import defaultdict
from sys import stdin


def n_boxes(grid, n_rows, n_columns):
    fibration = defaultdict(set)
    max_height = 0
    for i in range(n_rows):
        for j in range(n_columns):
            height = grid[i][j]
            fibration[height].add((i, j))
            if height > max_height:
                max_height = height

    result = 0
    height = max_height
    min_height = max_height - n_rows - n_columns + 2
    count = 0
    while True:
        while not fibration[height]:
            height -= 1
            if height < min_height:
                return result
        i, j = fibration[height].pop()
        neighbours = [
            (k, l)
            for (k, l) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            if 0 <= k < n_rows
            and 0 <= l < n_columns
            and (k, l) in fibration[grid[k][l]]
        ]
        for k, l in neighbours:
            fibration[grid[k][l]].remove((k, l))
            delta = max(0, grid[i][j] - grid[k][l] - 1)
            result += delta
            grid[k][l] += delta
            fibration[grid[k][l]].add((k, l))
        count += 1


n_tests = int(next(stdin))

for i in range(1, n_tests + 1):
    n_rows, n_columns = [int(x) for x in next(stdin).split()]
    grid = [[int(x) for x in next(stdin).split()] for _ in range(n_rows)]
    result = n_boxes(grid, n_rows, n_columns)
    print(f"Case #{i}: {result}")
