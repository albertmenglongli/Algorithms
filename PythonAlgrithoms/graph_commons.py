from collections import defaultdict


def transpose(G):
    GT = defaultdict(set)
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT


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


def walk(G, u, seen):
    res = {u}

    def recurse(u):
        for v in G[u]:
            if v in seen:
                continue
            else:
                seen.add(v)
                res.add(v)
                recurse(v)

    recurse(u)
    return res
