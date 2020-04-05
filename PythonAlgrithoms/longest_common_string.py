def memo(func):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return inner


def rec_lcs(a, b):
    @memo
    def L(i, j):
        if min(i, j) < 0:
            return 0
        if a[i] == b[j]:
            return 1 + L(i - 1, j - 1)
        else:
            return max(L(i - 1, j), L(i, j - 1))

    return L(len(a) - 1, len(b) - 1)


def lcs_dp(a, b):
    n, m = len(a), len(b)
    cur, pre = [0] * (n + 1), [0] * (n + 1)

    for j in range(1, m + 1):
        cur, pre = pre, cur
        for i in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                cur[i] = pre[i - 1] + 1
            else:
                cur[i] = max(cur[i - 1], pre[i])

    return cur[n]


if __name__ == '__main__':
    assert rec_lcs('starwalker', 'starbuck') == 5
    assert rec_lcs('spock', 'asoka') == 3

    assert lcs_dp('starwalker', 'starbuck') == 5
    assert lcs_dp('spock', 'asoka') == 3
