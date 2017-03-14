def components(G):
    def walk(s, F=set()):
        P, Q = dict(), set()
        P[s] = None
        Q.add(s)
        while Q:
            u = Q.pop()
            for v in G[u].difference(P, F):
                Q.add(v)
                P[v] = u
        return P

    comp = []
    seen = set()
    for u in G:
        if u in seen:
            continue
        C = walk(u)
        seen.update(C)
        comp.append(C)
    return comp


G = {
    'a': {'b', 'c', 'd'},
    'b': {'a', 'd'},
    'c': {'a', 'd'},
    'd': {'a', 'b', 'c'},
    'e': {'f', 'g'},
    'f': {'e', 'g'},
    'g': {'f', 'e'},
    'h': {'i'},
    'i': {'h'}
}

print components(G)