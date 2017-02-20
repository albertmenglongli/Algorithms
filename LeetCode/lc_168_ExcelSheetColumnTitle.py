class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        my_mapping = map(chr, range(ord('A'), ord('Z') + 1))
        result = ''
        while n:
            result = my_mapping[(n - 1) % 26] + result
            n = (n - 1) / 26
        return result


assert Solution().convertToTitle(0) == ''
assert Solution().convertToTitle(1) == 'A'
assert Solution().convertToTitle(26) == 'Z'
assert Solution().convertToTitle(27) == 'AA'
