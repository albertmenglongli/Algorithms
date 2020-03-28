def total_path_count_rec(m, n):
    if m == 1 and n == 1:
        return 0
    elif m == 1 or n == 1:
        return 1
    else:
        return total_path_count_rec(m - 1, n) + total_path_count_rec(m, n - 1)


def total_path_count_dp(m, n):
    assert m >= 1 and n >= 1
    cache = [[0] * n for __ in range(m)]
    cache[0][0] = 0
    for i in range(1, n):
        cache[0][i] = 1
    for i in range(1, m):
        cache[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            cache[i][j] = cache[i][j - 1] + cache[i - 1][j]

    return cache[m - 1][n - 1]


if __name__ == '__main__':
    print(total_path_count_rec(2, 2))
    print(total_path_count_rec(3, 3))
    print(total_path_count_rec(3, 4))

    print(total_path_count_dp(2, 2))
    print(total_path_count_dp(3, 3))
    print(total_path_count_dp(3, 4))
