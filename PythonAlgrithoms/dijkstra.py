from heapq import heappush, heappop

G = {
    'a': {
        'b': 2,
        'c': 1,
        'd': 3,
        'e': 9,
        'f': 4,
    },
    'b': {
        'c': 4,
        'e': 3,
    },
    'c': {
        'd': 8,
    },
    'd': {
        'e': 7,
    },
    'e': {
        'f': 5,
    },
    'f': {
        'c': 2,
        'g': 2,
        'h': 2,
    },
    'g': {
        'f': 1,
        'h': 6,
    },
    'h': {
        'g': 8,
        'f': 9,
    }
}

inf = float('inf')


def relax(W, u, v, D, P):
    d = D.get(u, inf) + W[u][v]
    if d < D.get(v, inf):
        D[v], P[v] = d, u
        return True
    return False


def dijkstra(G, s):
    D, P, Q, S = {s: 0}, {}, [(0, s)], set()

    while Q:
        __, u = heappop(Q)
        if u in S: continue
        S.add(u)
        for v in G[u]:
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))

    return D, P


def idijkstra(G, s):
    Q, S = [(0, s)], set()
    while Q:
        d, u = heappop(Q)
        if u in S: continue
        S.add(u)
        yield u, d
        for v in G[u]:
            heappush(Q, (d + G[u][v], v))


print(dijkstra(G, 'a'))

for item in idijkstra(G, 'a'):
    print(item)
