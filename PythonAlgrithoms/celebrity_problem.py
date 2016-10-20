def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if G[u][v]:
                break
            if not G[v][u]:
                break
        else:
            return u
    return None


def celeb(G):
    # the precondition is that there's only one celebrity
    n = len(G)
    u, v = 0, 1

    for c in range(2, n + 1):
        if G[u][v]:
            u = c
        else:
            v = c
    if u == n:
        c = v
    else:
        c = u

    for v in range(n):
        if v == c:
            continue
        if G[c][v]:
            break
        if not G[v][c]:
            break
    else:
        return c
    return None


def main():
    from random import randrange
    n = 1000
    G = [[randrange(2) for _ in range(n)] for _ in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = 1
        G[c][i] = 0

    print c
    print naive_celeb(G)
    print celeb(G)


if __name__ == '__main__':
    main()
