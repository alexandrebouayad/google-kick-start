from sys import stdin


def n_operations(string, n, k):
    score = sum(string[i] != string[-1 - i] for i in range(n // 2))
    return abs(score - k)


n_tests = int(next(stdin))

for i in range(1, n_tests + 1):
    n, k = [int(x) for x in next(stdin).split()]
    string = next(stdin).rstrip()
    n_ops = n_operations(string, n, k)
    print(f"Case #{i}: {n_ops}")
