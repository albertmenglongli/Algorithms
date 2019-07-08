def naive_topsort(G, S=None):
    if not S: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    seq = naive_topsort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]: min_i = i + 1
    seq.insert(min_i, v)
    return seq


def topsort(G):
    count = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1

    Q = [u for u in G if count[u] == 0]
    S = []
    while Q:
        u = Q.pop()
        S.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                Q.append(v)
    return S


def dfs_topsort(G):
    S, res = set(), []

    def recurse(u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)

    for u in G:
        recurse(u)
    res.reverse()
    return res


def main():
    G = {
        'd': ['e', 'f'],
        'f': [],
        'a': ['b', 'f'],
        'b': ['c', 'd', 'f'],
        'c': ['d'],
        'e': ['f'],

    }
    print(naive_topsort(G))
    print(topsort(G))
    print(dfs_topsort(G))


if __name__ == "__main__":
    main()
