from sys import stdin


def segments(grid, left=True):
    grid = grid if left else [lst[::-1] for lst in grid]
    segments = []
    for row in grid:
        lst = []
        count = 0
        for x in row:
            count = count + 1 if x else 0
            lst.append(count)
        segments.append(lst)
    segments = segments if left else [lst[::-1] for lst in segments]
    return segments


def n_lshapes(grid, n_rows, n_columns):
    transposed_grid = [[row[i] for row in grid] for i in range(n_columns)]
    left_segments = segments(grid)
    right_segments = segments(grid, left=False)
    up_segments = segments(transposed_grid)
    down_segments = segments(transposed_grid, left=False)

    return sum(
        max(min(h_segments[i][j], v_segments[j][i] // 2) - 1, 0)
        + max(min(h_segments[i][j] // 2, v_segments[j][i]) - 1, 0)
        for i in range(n_rows)
        for j in range(n_columns)
        for h_segments in (left_segments, right_segments)
        for v_segments in (up_segments, down_segments)
    )


n_tests = int(next(stdin))

for i in range(1, n_tests + 1):
    n_rows, n_columns = [int(x) for x in next(stdin).split()]
    grid = [[int(x) for x in next(stdin).split()] for _ in range(n_rows)]
    result = n_lshapes(grid, n_rows, n_columns)
    print(f"Case #{i}: {result}")
