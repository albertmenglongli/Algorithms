class Solution(object):
    @staticmethod
    def integerBreak(n):
        """
        :type n: int
        :rtype: int
        >>> for i in range(5, 12):
        ...     Solution.integerBreak(i)
        ...
        6
        9
        12
        18
        27
        36
        54
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
