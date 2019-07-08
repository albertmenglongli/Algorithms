def traverse_generator(G, s, qtype=set):
    Seen, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in Seen:
            continue
        Seen.add(u)
        for v in G[u]:
            Q.add(v)
        yield u


def traverse(G, s, qtype=set):
    Seen, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in Seen:
            continue
        Seen.add(u)
        for v in G[u]:
            Q.add(v)
    return Seen


G = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'd'],
    'c': ['a', 'd'],
    'd': ['a', 'b', 'c', 'e'],
    'e': ['f', 'g'],
    'f': ['e'],
    'g': ['e']
}

print(list(traverse_generator(G, 'a')))


class stack(list):
    add = list.append


print(list(traverse_generator(G, 'a', stack)))
