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


def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])  # Path compression
    return C[u]


def union(C, R, u, v):
    u = find(C, u)
    v = find(C, v)
    """
       The above operations can be optimized to O(Log n) in worst case.
       The idea is to always attach smaller depth tree under the root of the deeper tree.
       This technique is called union by rank.
       The term rank is preferred instead of height because if path compression technique is used,
       then rank is not always equal to height. Also, size (in place of height) of trees can also be used as rank. 
       Using size as rank also yields worst case time complexity as O(Logn)
       """
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v

    if R[u] == R[v]:
        R[v] += 1


def naive_kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C = {u: u for u in G}
    R = {u: 0 for u in G}

    for __, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)

    return T


if __name__ == '__main__':
    T = naive_kruskal(G)
    print(sorted(T))
