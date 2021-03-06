class Solution(object):
    @staticmethod
    def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        >>> print(Solution.generate(5))
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        """
        result = list()
        if numRows == 0: return result
        for i in range(numRows):
            row = list()
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result[i - 1][j - 1] + result[i - 1][j])
            result.append(row)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
