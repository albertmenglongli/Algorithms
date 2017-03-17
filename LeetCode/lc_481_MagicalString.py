class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = [1, 2, 2]
        idx = 2
        while len(S) < n:
            S.extend(S[idx] * [3 - S[-1]])
            idx += 1
        return S[:n].count(1)

