
def celeb(G):
    # the precondition is that there's only one celebrity
    n = len(G)
    u, v = 0, 1
    for c in range(2, n + 1):
        if G[u][v]:
            u = c
        else:
            v = c
    if u==n: 

    pass


def main():
    from random import randrange
    n = 100
    G = [[randrange(2) for _ in range(n)] for _ in range(n)]
    c = randrange(n)
    for i in range(c):
        G[i][c] = 1
        G[c][i] = 0
    print G
if __name__ == '__main__':
    main()
