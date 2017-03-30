class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        from heapq import heappush, heappop
        from itertools import repeat

        projects_heap = list()
        doable_projects_heap = list()

        map(heappush, repeat(projects_heap, len(Profits)), ((c, (p, c)) for p, c in zip(Profits, Capital)))

        # define some functions to get data from heap element
        get_profit_capital = lambda p: p[1]
        get_profit = lambda p: get_profit_capital(p)[0]
        get_capital = lambda p: get_profit_capital(p)[1]
        heappeek = lambda heap: heap[0]

        for i in range(0, k):
            while projects_heap and get_capital(heappeek(projects_heap)) <= W:
                p, c = get_profit_capital(heappop(projects_heap))
                heappush(doable_projects_heap, (-p, (p, c)))
            if not doable_projects_heap:
                break
            W += get_profit(heappop(doable_projects_heap))
        return W


# print(Solution().findMaximizedCapital(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1]))
print(Solution().findMaximizedCapital(k=3, W=0, Profits=[2, 2, 3], Capital=[0, 2, 4]))
