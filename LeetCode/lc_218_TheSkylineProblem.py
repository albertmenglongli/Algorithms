class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.divide_conquer(buildings)

    def divide_conquer(self, buildings):
        if not buildings:
            return []
        if len(buildings) == 1:
            b = buildings[0]
            return [[b[0], b[2]], [b[1], 0]]

        mid = len(buildings) // 2
        left = self.divide_conquer(buildings[:mid])
        right = self.divide_conquer(buildings[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        from collections import deque
        res = []
        h1 = h2 = 0
        left = deque(left)
        right = deque(right)
        while left and right:
            x = h = 0
            if left[0][0] < right[0][0]:
                x, h1 = left.popleft()
                h = max(h1, h2)
            elif left[0][0] > right[0][0]:
                x, h2 = right.popleft()
                h = max(h1, h2)
            else:
                x, h1 = left.popleft()
                x, h2 = right.popleft()
                h = max(h1, h2)

            if not res or h != res[-1][1]:
                res.append([x, h])

        res.extend(list(left) + list(right))
        return res


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
assert Solution().getSkyline(buildings=buildings) == [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
