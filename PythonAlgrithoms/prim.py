from heapq import heappop, heappush


def prim(G, s):
    P, Q = {}, [(0, None, s)]

    while Q:
        _, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        for v, w in G[u].items():
            heappush(Q, (w, u, v))
    return P


