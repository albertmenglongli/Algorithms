class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        table = [0] * 26
        cur_max = 0
        for i, value in enumerate(p):
            if i > 0 and (ord(p[i - 1]) + 1) % 26 == ord(value) % 26:
                cur_max += 1
            else:
                cur_max = 1
            table[ord(value) - ord('a')] = max(table[ord(value) - ord('a')], cur_max)
        return sum(table)


print(Solution().findSubstringInWraproundString("zab"))
