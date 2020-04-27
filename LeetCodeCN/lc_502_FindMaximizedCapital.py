from typing import List


# from functools import cmp_to_key
# from functools import lru_cache
#
#
# def cmp_func(a, b):
#     if a[0] < b[0]:
#         return -1
#     elif a[0] > b[0]:
#         return 1
#     if a[1] > b[1]:
#         return -1
#     elif a[1] < b[1]:
#         return 1
#
#     return 0


# 标准的递归版本0-1背包解法，会超时
# class Solution:
#     def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
#
#         capital_profit = list(zip(Capital, Profits))
#         capital_profit.sort(key=cmp_to_key(cmp_func))
#
#         @lru_cache()
#         def foo(i, _w, _k):
#             if i == len(Profits) or _k == k:
#                 return _w
#             drop = foo(i + 1, _w, _k)
#             if _w < capital_profit[i][0]:
#                 # cannot start the project
#                 return drop
#             # including the i project
#             _w += capital_profit[i][1]
#             return max(drop, foo(i + 1, _w, _k + 1))
#
#         return foo(0, W, 0)


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        n = len(Profits)
        for i in range(min(n, k)):
            idx = -1
            for j in range(n):
                if W >= Capital[j]:
                    if idx == -1:
                        idx = j
                    elif Profits[idx] < Profits[j]:
                        idx = j

            if idx == -1:
                break

            W += Profits[idx]
            Capital[idx] = float('inf')

        return W


if __name__ == '__main__':
    k = 2
    W = 0
    Profits = [1, 2, 3]
    Capital = [0, 1, 1]

    print(Solution().findMaximizedCapital(k, W, Profits, Capital))

    k = 10
    W = 0
    Profits = [1, 2, 3]
    Capital = [0, 1, 2]

    print(Solution().findMaximizedCapital(k, W, Profits, Capital))

    k = 1
    W = 2
    Profits = [1, 2, 3]
    Capital = [1, 1, 2]

    print(Solution().findMaximizedCapital(k, W, Profits, Capital))
