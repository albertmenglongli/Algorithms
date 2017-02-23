class SolutionRecursion(object):
    def min_path_cost(self, cost, m, n):
        return self._min_path_cost(cost, m, n)

    def _min_path_cost(self, cost, m, n):
        if m == 0 and n == 0:
            return cost[0][0]
        elif m == 0:
            return self._min_path_cost(cost, 0, n - 1) + cost[0][n]
        elif n == 0:
            return self._min_path_cost(cost, m - 1, 0) + cost[m][0]
        else:
            x = self._min_path_cost(cost, m, n - 1)
            y = self._min_path_cost(cost, m - 1, n)
            return min(x, y) + cost[m][n]


class SolutionRecursionMemo(object):
    def min_path_cost(self, cost, m, n):
        self.mem = [[0] * (n + 1) for _ in range(m + 1)]
        return self._min_path_cost(cost, m, n)

    def _min_path_cost(self, cost, m, n):
        if self.mem[m][n]:
            return self.mem[m][n]
        if m == 0 and n == 0:
            self.mem[m][n] = cost[0][0]
        elif m == 0:
            self.mem[m][n] = self._min_path_cost(cost, 0, n - 1) + cost[0][n]
        elif n == 0:
            self.mem[m][n] = self._min_path_cost(cost, m - 1, 0) + cost[m][0]
        else:
            x = self._min_path_cost(cost, m, n - 1)
            y = self._min_path_cost(cost, m - 1, n)
            self.mem[m][n] = min(x, y) + cost[m][n]
        return self.mem[m][n]


class SolutionBottomUpDP(object):
    def min_path_cost(self, cost, m, n):
        memo = dict()
        memo[0, 0] = cost[0][0]
        for i in range(1, n + 1):
            memo[0, i] = memo[0, i - 1] + cost[0][i]
        for j in range(1, m + 1):
            memo[j, 0] = memo[j - 1, 0] + cost[j][0]
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                memo[j, i] = min(memo[j - 1, i], memo[j, i - 1]) + cost[j][i]
        return memo[m, n]


cost = [[1, 3, 5, 8],
        [4, 2, 1, 7],
        [4, 3, 2, 3],
        ]

print SolutionRecursionMemo().min_path_cost(cost, len(cost) - 1, len(cost[0]) - 1)
print SolutionRecursion().min_path_cost(cost, len(cost) - 1, len(cost[0]) - 1)
print SolutionBottomUpDP().min_path_cost(cost, len(cost) - 1, len(cost[0]) - 1)
