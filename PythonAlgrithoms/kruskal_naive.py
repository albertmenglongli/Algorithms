G = {
    'A': {
        'B': 7,
        'D': 5,
    },
    'B': {
        'A': 7,
        'C': 8,
        'D': 9,
        'E': 7,
    },
    'C': {
        'B': 8,
        'E': 5,
    },
    'D': {
        'A': 5,
        'B': 9,
        'E': 15,
        'F': 6,
    },
    'E': {
        'B': 7,
        'C': 5,
        'D': 15,
        'F': 8,
        'G': 9,
    },
    'F': {
        'D': 6,
        'E': 8,
        'G': 11,
    },
    'G': {
        'E': 9,
        'F': 11,
    }
}


def naive_find(C, u):
    while C[u] != u:  # at the top, C[root] = root
        u = C[u]
    return u


def naive_union(C, u, v):
    u = naive_find(C, u)
    v = naive_find(C, v)
    C[u] = v


def naive_kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C = {u: u for u in G}

    for __, u, v in sorted(E):
        if naive_find(C, u) != naive_find(C, v):
            T.add((u, v))
            naive_union(C, u, v)

    return T


if __name__ == '__main__':
    T = naive_kruskal(G)
    print(sorted(T))
