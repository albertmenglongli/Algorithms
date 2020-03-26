cost = [
    [0, 10, 75, 94],
    [-1, 0, 35, 50],
    [-1, -1, 0, 80],
    [-1, -1, -1, 0],
]


def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def rec_cal_min_cost(s, d):
    global cost
    if s == d or s == d - 1:
        return cost[s][d]
    min_cost = cost[s][d]
    for i in range(s + 1, d):
        temp = rec_cal_min_cost(s, i) + rec_cal_min_cost(i, d)
        if temp < min_cost:
            min_cost = temp
    return min_cost


def dp_cal_min_cost():
    global cost
    n = len(cost)
    minCost = [float('inf')] * n
    minCost[0] = 0
    minCost[1] = cost[0][1]

    for i in range(2, n):
        minCost[i] = cost[0][i]
        for j in range(1, i):
            if minCost[i] > minCost[j] + cost[j][i]:
                minCost[i] = minCost[j] + cost[j][i]
    return minCost[n - 1]


if __name__ == '__main__':
    print(rec_cal_min_cost(0, 3))
    print(dp_cal_min_cost())
