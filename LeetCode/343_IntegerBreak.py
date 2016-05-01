class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        cnt = n / 3
        mod = n % 3
        import math
        if mod == 0:
            return int(math.pow(3, cnt))
        elif mod == 1:
            return int(math.pow(3, cnt - 1)) * 4
        elif mod == 2:
            return int(math.pow(3, cnt)) * 2
