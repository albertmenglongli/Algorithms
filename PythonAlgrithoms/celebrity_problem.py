# -*- coding:utf-8 -*-
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
    # 此算法主要是通过排除法, 排除掉不可能的值, 最后剩下一个可能的候选人
    n = len(G)
    u, v = 0, 1

    # 类比猜拳, 有一个人总是赢(或总是输), 我们要把他选出来
    # 每次拿两个人上台比较一下, 不符合条件的人下场, 换新人与之前的人继续较量, 直到最终把这个候选人选出来
    for i in range(2, n + 1):
        # G[u][v]中 u, v 的值,都是之前循环中的 i 赋予的,所以 i = n 的时候, G[u][v] 不会数组越界
        if G[u][v]:
            u = i
        else:
            v = i
    if u == n:
        # 该算法中, 实际的数组索引范围是range(0, n)即 0 -> n-1,
        # n 实际上是一个不合法的值, 为n只能说明之前的 u 对应的参赛者值已经被排除掉, v 自然成为了可能的候选者
        # c 代表candidate候选者
        c = v
    else:
        # 如果 v == n 的情况(此处, for i in range(2, n+1) 保证了: 最后循环结束时不是u = n , 就是v = n), 同上 u 成为了候选者
        c = u

    # 最后判断一下, 剩下的这个候选者, 是否满足条件(用其他所有的人都与之判断一次, 一个for-loop)
    for i in range(n):
        if i == c:
            continue
        if G[c][i]:
            break
        if not G[i][c]:
            break
    else:
        return c
    return None


def main():
    from random import randrange
    n = 10
    G = [[randrange(2) for _ in range(n)] for _ in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = 1
        G[c][i] = 0

    # print c
    # print naive_celeb(G)
    print celeb(G)


if __name__ == '__main__':
    main()
