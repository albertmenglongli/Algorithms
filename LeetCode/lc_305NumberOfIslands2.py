class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        self.m = m
        self.n = n
        self.table = [[None] * n for _ in range(m)]
        self.rank = [[0] * n for _ in range(m)]
        self.cnt = 0
        result = []
        for pos in positions:
            self.look_around_and_union(pos)
            result.append(self.cnt)
        return result

    def look_around_and_union(self, p):
        x, y = p
        self.table[x][y] = p
        self.cnt += 1
        points_to_union = []
        if y - 1 >= 0 and self.table[x][y - 1] is not None:
            points_to_union.append([x, y-1])
        if y + 1 < self.n and self.table[x][y + 1] is not None:
            points_to_union.append([x, y+1])
        if x - 1 >= 0 and self.table[x - 1][y] is not None:
            points_to_union.append([x-1, y])
        if x + 1 < self.m and self.table[x + 1][y] is not None:
            points_to_union.append([x+1, y])
        if points_to_union:
            self.union(p, points_to_union[0])
            if len(points_to_union) >= 2:
                for i in range(1, len(points_to_union)):
                    self.union(points_to_union[i], p)

    def find(self, p):
        x, y = p
        if self.table[x][y] is None:
            return None
        if self.table[x][y] == p:
            return p
        else:
            return self.find(self.table[x][y])

    def union(self, p1, p2):
        p1_root = self.find(p1)
        p2_root = self.find(p2)
        if self.find(p1) != self.find(p2):
            self.cnt -= 1
            self.table[p1_root[0]][p1_root[1]] = p2_root


print Solution().numIslands2(m=3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 1]])
print Solution().numIslands2(3, 3, [[0, 1], [1, 2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]])
