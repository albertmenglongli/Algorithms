class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (D - B) * (C - A)
        area2 = (H - F) * (G - E)
        width = self.len_overlap((A, C), (E, G))
        height = self.len_overlap((B, D), (F, H))
        overlap = width * height
        return area1 + area2 - overlap

    def len_overlap(self, r1, r2):
        a, b = r1
        c, d = r2
        if b > c and a < d:
            return min(b, d) - max(a, c)
        return 0


print Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
