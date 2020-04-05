from functools import lru_cache


def rec_unbounded_knapsack(w, v, c):
    @lru_cache(None)
    def m(r):
        if r == 0: return 0
        val = m(r - 1)
        for i, wi in enumerate(w):
            if wi > r: continue
            val = max(val, m(r - wi) + v[i])
        return val

    return m(c)


def unbounded_knapsack(w, v, c):
    m = [0]

    for r in range(1, c + 1):
        val = m[r - 1]
        for i, wi in enumerate(w):
            if wi > r: continue
            val = max(val, v[i] + m[r - wi])
        m.append(val)
    return m[c]


def rec_knapsack(w, v, c):
    @lru_cache()
    def m(k, r):
        if k == 0 or r == 0: return 0
        i = k - 1
        drop = m(k - 1, r)
        if w[i] > r: return drop
        return max(drop, v[i] + m(k - 1, r - w[i]))

    return m(len(w), c)


def knapsack(w, v, c):
    n = len(w)
    m = [[0] * (c + 1) for __ in range(n + 1)]
    P = [[False] * (c + 1) for __ in range(n + 1)]
    for k in range(1, n + 1):
        i = k - 1
        for r in range(1, c + 1):
            m[k][r] = drop = m[k - 1][r]
            if w[i] > r: continue
            keep = v[i] + m[k][r - w[i]]
            m[k][r] = max(drop, keep)
            P[k][r] = keep > drop

    return m, P
