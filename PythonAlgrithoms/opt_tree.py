from functools import lru_cache


def rec_opt_tree(p):
    @lru_cache()
    def s(i, j):
        if i == j: return 0
        return s(i, j - 1) + p[j - 1]

    @lru_cache()
    def e(i, j):
        if i == j: return 0
        sub = min(e(i, r) + e(r, j) for r in range(i, j))
        return sub + s(i, j)

    return e(0, len(p))


from collections import defaultdict


def opt_tree(p):
    n = len(p)
    s, e = defaultdict(int), defaultdict(int)

    for l in range(1, n + 1):
        for i in range(n + 1 - l):
            j = i + l  # i+j+l <= n+1

            s[i, j] = s[i, j - 1] + p[j - 1]
            e[i, j] = min(e[i, r] + e[r, j] for r in range(i, j))
            e[i, j] += s[i, j]
    return e[0, n]
